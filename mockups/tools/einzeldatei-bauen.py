"""Alle Mockups in EINE HTML-Datei packen (zum Hochladen und Weitergeben).

Jede Seite wird mit ihren Stylesheets, Schriften, Bildern und Skripten eingebettet und in
einer Hülle per iframe angezeigt. Links zwischen den Seiten, Pfeiltasten und Zurück-Taste
funktionieren wie im Ordner. Die Datei braucht weder Server noch Internet.

    python mockups/tools/einzeldatei-bauen.py

Ergebnis: dist/PRINT-BITE-Mockups.html (Repo-Wurzel). Benötigt Pillow.
"""

import base64
import io
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT.parent / "dist" / "PRINT-BITE-Mockups.html"
PAGES = [
    "index",
    "m1-original",
    "m2-retro-konditorei",
    "m3-pistazie-rose",
    "m4-aprikose-editorial",
    "m5-filament-labor",
]
PHOTO_MAX_WIDTH = 1000

# Läuft in jeder eingebetteten Seite: Seitenlinks an die Hülle melden, Anker im Dokument scrollen.
BRIDGE = """<script>
(function () {
  document.addEventListener("click", function (event) {
    var link = event.target.closest("a[href]");
    if (!link) return;
    var href = link.getAttribute("href");
    var page = href.match(/^([\\w-]+)\\.html(#[\\w-]+)?$/);
    if (page) {
      event.preventDefault();
      parent.postMessage({ pb: "go", page: page[1], anchor: page[2] || "" }, "*");
    } else if (/^#[\\w-]+$/.test(href)) {
      var target = document.getElementById(href.slice(1));
      if (target) { event.preventDefault(); target.scrollIntoView({ behavior: "smooth" }); }
    } else if (/^https?:/.test(href)) {
      link.target = "_blank";
      link.rel = "noopener";
    }
  });
  window.addEventListener("message", function (event) {
    var data = event.data;
    if (!data || data.pb !== "scroll") return;
    var target = document.getElementById(data.anchor.slice(1));
    if (target) target.scrollIntoView({ behavior: data.smooth ? "smooth" : "auto" });
  });
  parent.postMessage({ pb: "ready", title: document.title }, "*");
})();
</script>"""

SHELL = """<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>PRINT&amp;BITE - Designrichtungen (Mockups)</title>
  <style>
    html, body { margin: 0; height: 100%; background: #f4f4f1; font: 16px/1.5 system-ui, sans-serif; color: #1c1b1f; }
    iframe { position: fixed; inset: 0; width: 100%; height: 100%; border: 0; display: block; }
    noscript p { max-width: 36rem; margin: 3rem auto; padding: 0 1rem; }
  </style>
</head>
<body>
  <noscript><p>Diese Datei zeigt die Website-Entwürfe von PRINT&amp;BITE. Bitte in einem Browser wie Chrome, Edge, Firefox oder Safari öffnen und JavaScript erlauben.</p></noscript>
  <iframe id="ansicht" title="PRINT&amp;BITE Mockups" allow="clipboard-write"></iframe>
  <script>
    (function () {
      var PAGES = __PAGES__;
      var frame = document.getElementById("ansicht");
      var current = null;
      var pendingAnchor = "";

      // Nur Nachrichten statt contentDocument: unter file:// darf die Hülle das Iframe-Dokument evtl. nicht lesen.
      function show(page, anchor) {
        if (!PAGES[page]) page = "index";
        if (page !== current) {
          current = page;
          pendingAnchor = anchor;
          frame.srcdoc = PAGES[page];
        } else if (anchor) {
          frame.contentWindow.postMessage({ pb: "scroll", anchor: anchor, smooth: true }, "*");
        }
      }

      function fromHash() {
        var page = decodeURIComponent(location.hash.slice(1)) || "index";
        show(page, "");
      }

      window.addEventListener("message", function (event) {
        var data = event.data;
        if (!data || event.source !== frame.contentWindow) return;
        if (data.pb === "ready") {
          document.title = data.title;
          if (pendingAnchor) frame.contentWindow.postMessage({ pb: "scroll", anchor: pendingAnchor }, "*");
          pendingAnchor = "";
          frame.contentWindow.focus();
          return;
        }
        if (data.pb !== "go") return;
        if (location.hash.slice(1) !== data.page) {
          location.hash = data.page;
        }
        show(data.page, data.anchor);
      });
      window.addEventListener("hashchange", fromHash);
      fromHash();
    })();
  </script>
</body>
</html>
"""


def data_uri(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in (".jpg", ".jpeg"):
        image = Image.open(path).convert("RGB")
        if image.width > PHOTO_MAX_WIDTH and "vorschau" not in path.name:
            image = image.resize((PHOTO_MAX_WIDTH, round(image.height * PHOTO_MAX_WIDTH / image.width)), Image.LANCZOS)
        buffer = io.BytesIO()
        image.save(buffer, "JPEG", quality=78, optimize=True, progressive=True)
        mime, raw = "image/jpeg", buffer.getvalue()
    elif suffix == ".png":
        buffer = io.BytesIO()
        Image.open(path).save(buffer, "WEBP", quality=88, method=6)
        mime, raw = "image/webp", buffer.getvalue()
    elif suffix == ".woff2":
        mime, raw = "font/woff2", path.read_bytes()
    else:
        raise ValueError(f"unbekannter Dateityp: {path}")
    return f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"


_cache = {}


def asset(path: Path) -> str:
    if path not in _cache:
        _cache[path] = data_uri(path)
    return _cache[path]


def font_faces(used_text: str) -> str:
    """Nur die @font-face-Blöcke der Schriften, die die Seite tatsächlich nennt."""
    css = (ROOT / "assets" / "fonts" / "fonts.css").read_text(encoding="utf-8")
    blocks = re.findall(r"@font-face \{.*?\}", css, re.S)
    out = []
    for block in blocks:
        family = re.search(r"font-family: '(.*?)'", block).group(1)
        if family in used_text:
            src = re.search(r"url\(\./(.*?)\)", block).group(1)
            out.append(block.replace(f"./{src}", asset(ROOT / "assets" / "fonts" / src)))
    return "\n".join(out)


def build_page(name: str) -> str:
    html = (ROOT / f"{name}.html").read_text(encoding="utf-8")
    sheets = re.findall(r'<link rel="stylesheet" href="([^"]+)">', html)
    css_parts = [(ROOT / href).read_text(encoding="utf-8") for href in sheets if "fonts.css" not in href]
    css = "\n".join(css_parts)
    fonts = font_faces(css + html)
    first = True

    def replace_link(match):
        nonlocal first
        if first:
            first = False
            return f"<style>\n{fonts}\n{css}\n</style>"
        return ""

    html = re.sub(r'<link rel="stylesheet" href="[^"]+">', replace_link, html)
    script = (ROOT / "design-system" / "mockup.js").read_text(encoding="utf-8")
    html = html.replace('<script src="design-system/mockup.js" defer></script>', "")
    html = html.replace("</body>", f"<script>\n{script}\n</script>\n{BRIDGE}\n</body>")
    html = re.sub(r'(src|href)="(assets/[^"]+)"', lambda m: f'{m.group(1)}="{asset(ROOT / m.group(2))}"', html)
    if "assets/" in re.sub(r"data:[^\"')]+", "", html):
        raise SystemExit(f"{name}: nicht eingebettete Asset-Referenz übrig")
    return html


def main() -> None:
    pages = {name: build_page(name) for name in PAGES}
    payload = json.dumps(pages, ensure_ascii=False).replace("</", "<\\/")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(SHELL.replace("__PAGES__", payload), encoding="utf-8")
    print(f"{OUT} ({OUT.stat().st_size / 1_000_000:.1f} MB)")


if __name__ == "__main__":
    main()
