# Mockups: Designrichtung PRINT&BITE

Fünf Varianten der Startseite für das Treffen mit der Schülerfirma am 02.10.2026. Ticket: [Designrichtung wählen: 5 Mockups für das Treffen am 02.10.](https://github.com/HAITI-03-Messeretter/print-and-bite/issues/3).

## Ansehen

`index.html` per Doppelklick im Browser öffnen. Kein Server, kein Build, keine Internetverbindung nötig. Von dort sind alle Varianten verlinkt; in jeder Variante wechseln die Pfeiltasten ← → zur nächsten.

| Datei | Variante | Idee |
| --- | --- | --- |
| `m1-original.html` | M1 Original | Wireframe, Farben und Schriften der Schülerfirma eins zu eins |
| `m2-retro-konditorei.html` | M2 Retro-Konditorei | gleiche Farben, Kontrast korrigiert, Sticker-Look |
| `m3-pistazie-rose.html` | M3 Pistazie & Rose | Rosé und Marzipan plus Pistaziengrün, weiche Formen |
| `m4-aprikose-editorial.html` | M4 Aprikose Editorial | wärmer verschoben, ruhiges Magazin-Layout, Sie-Form |
| `m5-filament-labor.html` | M5 Filament-Labor | bewusster Kontrast: dunkel, Limette, technisches Raster |

### Als eine Datei weitergeben

```bash
python mockups/tools/einzeldatei-bauen.py
```

Packt alle Seiten mit Schriften, Bildern und Skripten in `dist/PRINT-BITE-Mockups.html` (ca. 6,6 MB, nicht im Repo). Die Datei per Doppelklick öffnen; Links, Pfeiltasten und Zurück-Taste funktionieren wie im Ordner. Gut zum Hochladen auf das TaskCards-Board.

Die Übersicht enthält außerdem Kontrastwerte der Originalfarben, einen Vergleich, einen Entscheidungsbogen (Ergebnis zum Kopieren) und die offenen Fragen an die Schülerfirma.

## Aufbau

```text
mockups/
  index.html               Übersicht und Entscheidungsbogen
  m1-...html bis m5-...html  die Varianten (alle direkt hier, damit file:// in jedem Browser funktioniert)
  design-system/
    tokens.css             Token-Vertrag mit neutralen Defaults
    base.css               Reset, Typografie, Layout
    components.css         Bausteine: ds-btn, ds-card, ds-event, ds-quiz, ds-header, ds-footer ...
    mockup.js              Scroll-Reveal, Quiz, Menü, Pfeiltasten
  themes/                  ein Theme je Variante (Tokens + Layout der Seite)
  assets/
    fonts/                 selbst gehostete Schriften (SIL Open Font License)
    icons/                 Phosphor Icons (MIT), werden inline ins HTML kopiert
    img/                   Produktfotos und freigestelltes Logo
    logo/                  Logo eingefärbt je Variante
  tools/logo-einfaerben.py Logo in einer Theme-Farbe exportieren
```

## Design-System anpassen

Drei Ebenen:

1. **Palette** (`--pal-*`): die Rohfarben einer Variante. Nur im Theme.
2. **Bedeutung** (`--color-bg`, `--color-primary`, `--font-display`, `--radius-btn`, `--shadow-btn` ...): was eine Farbe oder Form tut. Vollständige Liste mit Erklärung in `design-system/tokens.css`.
3. **Bausteine** (`components.css`): lesen ausschließlich Ebene 2.

Beispiel: Alle Buttons einer Variante eckig statt rund machen heißt im Theme `--radius-btn: 0;` setzen. Eine neue Variante entsteht, indem man ein Theme kopiert und die Tokens ändert.

Logo einfärben (braucht Pillow):

```bash
python mockups/tools/logo-einfaerben.py m6 "#3b1f2b"
```

## Bekannte Einschränkungen

- Fotos von Pizzaschnecken, Holzprodukten, Team, Aktionen und der Lageplan fehlen und sind als Platzhalter markiert.
- Termine sind Beispiele, Texte sind Entwürfe. Hinweistext, Kontakt per E-Mail-Link und Fotos ohne erkennbare Personen folgen der [Rechts-Recherche](https://github.com/HAITI-03-Messeretter/print-and-bite/issues/7); E-Mail-Adresse ist ein Platzhalter.
- Stay Retro (Lizenz nur privat) ist durch Leckerli One ersetzt, siehe [Schriftlizenzen](https://github.com/HAITI-03-Messeretter/print-and-bite/issues/6).
- Kein Dark Mode, keine Unterseiten: kommt nach der Entscheidung.
