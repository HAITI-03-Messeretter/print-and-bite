# Research: Schriftlizenzen Stay Retro, Pacifico, League Spartan

- Ticket: [#6](https://github.com/HAITI-03-Messeretter/print-and-bite/issues/6) (Teil der Map #2, blockiert #10)
- Stand: 01.10.2026 (Preise und Lizenztexte an diesem Tag abgerufen)
- Grundlage: Lizenztexte und Seiten der Rechteinhaber, SIL-OFL-Text und -FAQ, Google-Fonts-Repository, Urteilstext LG München I. Keine Rechtsberatung.

## Kurzantwort

| Schrift | Rolle (geplant) | Lizenz | Auf öffentlicher Website einbindbar? | Kosten |
| --- | --- | --- | --- | --- |
| Stay Retro (Din Studio) | Überschriften | proprietär, kostenlose Version nur private Nutzung | **Nein** mit der kostenlosen dafont-Version. **Ja** nur mit gekaufter Webfont License | ab **21 USD** einmalig (1 Domain, bis 10.000 Seitenaufrufe/Monat) |
| Pacifico | Fließtext | SIL Open Font License 1.1 | **Ja**, auch kommerziell, Self-Hosting erlaubt | 0 |
| League Spartan | Akzent | SIL Open Font License 1.1 | **Ja**, auch kommerziell, Self-Hosting erlaubt | 0 |

Empfehlung:

1. Stay Retro durch **Leckerli One** (OFL, kostenlos) ersetzen. Optisch am nächsten (Vergleich in Abschnitt 4).
2. Alle Schriften **selbst hosten** (gleiche Domain wie die Website), Format **WOFF2**, keine Einbindung über `fonts.googleapis.com` / `fonts.gstatic.com`.
3. Für #10 prüfen: Pacifico ist eine Handschrift-/Display-Schrift und als Fließtext schlecht lesbar (Hinweis in Abschnitt 2).

---

## 1. Stay Retro (Din Studio)

### 1.1 Lizenz laut Quellen

- **dafont** führt die Schrift als "Free for personal use". Die Autornotiz auf der Seite sagt sinngemäß: nur private Nutzung, kommerzielle Nutzung nicht erlaubt; wer mit der Schrift Geld verdient, soll eine Lizenz kaufen. Für Verstöße wird eine Gebühr in Höhe des Zehnfachen der Corporate License angedroht (10 x 1.999 USD). [Q1]
- dafont selbst stellt klar, dass die Lizenzangabe über dem Download-Button nur ein Hinweis ist; maßgeblich sind Readme und Website des Autors. [Q2]
- **Din Studio** (Rechteinhaber) unterscheidet auf seiner Lizenzseite [Q4]:
  - *Desktop License*: Installation auf Rechnern, kommerzielle Nutzung für **statische** Designs (Logos ohne Markenrechte, Flyer, Plakate, Verpackung, Etiketten, Menüs, "social media graphics (images only)"), Export als JPG, PNG, PDF, TIFF.
  - *Webfont License*: Nutzung auf **einer** Website/Domain, Einbindung per `@font-face`, monatliches Seitenaufruf-Limit je Stufe, "lifetime usage". Enthält zusätzlich alle Rechte der Desktop License.
  - Weitere Lizenzen (Merchandise, Branding & Logo, Corporate usw.) für Produkte, Markeneintragung, Unternehmensweit.
  - Keine Sonderregeln für Schulen, Bildung oder Non-Profit.
- Din-Studio-FAQ: `@font-face` nur auf einem Domainnamen; Fontdateien dürfen nicht weitergegeben oder zum Download angeboten werden. [Q5]
- Lieferumfang laut Produktseite: TTF, OTF, WOFF. [Q3] Din Studio empfiehlt in der eigenen Webfont-Anleitung, aus TTF/OTF mit einem Webfont-Generator ein Kit (u. a. WOFF2) zu erzeugen und selbst zu hosten. [Q6]

### 1.2 Einordnung für PRINT&BITE

- Die Schülerfirma verkauft Produkte und Snacks; die Website bewirbt diesen Verkauf. Das fällt unter "make money using this font", also **kommerzielle Nutzung**. [Q1]
- Unabhängig davon: Bei Webfont-Einbindung wird die Fontdatei an jeden Besucher ausgeliefert. Das deckt bei Din Studio nur die Webfont License ab; die Desktop License umfasst nur statische Designs (Bilder, PDFs, Drucksachen). [Q4]
- **Ergebnis:** Die kostenlose dafont-Version darf auf der öffentlichen Website weder per `@font-face` noch als Überschrift-Grafik verwendet werden.

### 1.3 Kosten (Shop Din Studio, Stand 01.10.2026, USD, einmalig) [Q3]

| Lizenz | Stufe | Preis |
| --- | --- | --- |
| Desktop License | 1 / 2 / 5 / 10 Nutzer | 12 / 18 / 30 / 50 USD |
| **Webfont License** | **10.000** / 100.000 / 500.000 / 1.000.000 Seitenaufrufe pro Monat | **21** / 40 / 85 / 150 USD |
| Merchandise License | 1.000 / 10.000 verkaufte Produkte | 49 / 100 USD |
| Branding & Logo License (exklusive Markenrechte) | 1 / 3 Marken | 329 / 560 USD |
| Corporate License | 1 Projekt | 1.999 USD |

### 1.4 Falls Stay Retro trotzdem bleiben soll

- **Webfont License, Stufe 10.000 Seitenaufrufe (21 USD)** reicht für eine Schülerfirmen-Website und deckt laut Lizenz auch Flyer, Plakate, Verpackung und Social-Media-Bilder (Desktop-Rechte). [Q4]
- Kauf durch Schule bzw. betreuende Lehrkraft im Namen der Schülerfirma, damit der Lizenznehmer eindeutig ist. Rechnung und Lizenznachweis aufbewahren.
- Lizenz gilt für **eine Domain**: auf die endgültige Domain beziehen; bei Domainwechsel mit Din Studio klären.
- Fontdateien nicht in ein öffentliches Repository legen (Weitergabeverbot [Q5]).
- Logo soll als Marke eingetragen werden: dann Branding & Logo License (329 USD). Ohne Markeneintragung ist ein Logo im Desktop-Umfang abgedeckt ("logos (without trademark rights)"). [Q4]
- Schrift erscheint auf verkauften Produkten (z. B. Schriftzug auf 3D-Druck-Artikeln, Sticker): Merchandise License prüfen (49 USD für 1.000 Produkte). [Q4]
- Günstiger Mittelweg: Nur den Logo-Schriftzug in Stay Retro als Grafik (PNG) ausliefern, Überschriften in einer freien Alternative setzen. Dafür reicht die Desktop License (12 USD). SVG ist in der Lizenz nicht ausdrücklich genannt; im Zweifel bei Din Studio nachfragen.

---

## 2. Pacifico

- Google-Fonts-Repository: Lizenz **OFL**, Designer Vernon Adams, Jacques Le Bailly, Botjo Nikoltchev, Ani Petrova, Kategorie "HANDWRITING". [Q7]
- Lizenzdatei: "Copyright 2018 The Pacifico Project Authors", SIL Open Font License 1.1, **kein Reserved Font Name**. [Q7]
- Die OFL erlaubt Nutzung, Veränderung und Weitergabe; verboten ist nur, die Schrift **für sich allein** zu verkaufen (Bedingung 1). Bei Weitergabe müssen Copyright-Hinweis und Lizenz beiliegen (Bedingung 2). [Q9]
- OFL-FAQ 2.1: Webfonts per `@font-face` sind ausdrücklich erlaubt, auch auf dem eigenen Server. [Q10]
- Google-Fonts-FAQ: Schriften dürfen kommerziell genutzt werden, auch in Logos und auf Websites. [Q11]
- Ohne Reserved Font Name ist Umwandlung (WOFF2) und Subsetting ohne Umbenennung erlaubt (OFL Bedingung 3 betrifft nur Reserved Font Names). [Q9]
- **Ergebnis:** nutzbar, kostenlos. Bedingung: `OFL.txt` neben die Fontdateien legen (OFL-FAQ 1.10: Lizenztext als eigene Datei oder in den Font-Metadaten). [Q10]
- **Hinweis für #10:** Pacifico ist eine verbundene Script-Schrift (Google-Kategorie "HANDWRITING"). Für Überschriften gut, für Fließtext (Absätze, Terminliste) schlecht lesbar. Sinnvoller: Fließtext in League Spartan oder einer anderen Sans. Pacifico sieht Stay Retro zudem recht ähnlich und könnte selbst die Überschriften übernehmen (zwei statt drei Schriften).

## 3. League Spartan

- Google-Fonts-Repository: Lizenz **OFL**, Designer Matt Bailey, Tyler Finck, Kategorie "SANS_SERIF", Quelle `theleagueof/league-spartan`. [Q8]
- Lizenzdatei: "Copyright 2020 The League Spartan Project Authors", SIL Open Font License 1.1, **kein Reserved Font Name**. [Q8]
- Variable Font mit Gewichtsachse 100 bis 900 (eine Datei `LeagueSpartan[wght].ttf` für alle Stärken). [Q8]
- **Ergebnis:** nutzbar, kostenlos, gleiche Bedingungen wie Pacifico.

---

## 4. Freie Alternativen für Stay Retro

Methode: Testzeile "Print&Bite leckere Snacks" mit allen Kandidaten gerendert (TTF aus dem Google-Fonts-Repository) und neben die dafont-Vorschau von Stay Retro gelegt. Stay Retro ist eine fette, leicht geneigte Script-Schrift mit runden, pinselartigen Strichen. Zusätzlich deutsche Sonderzeichen geprüft ("Äpfel, Öl, Übung, süß, Größe 5 €"): alle unten genannten Schriften enthalten Ä Ö Ü ä ö ü ß €.

| Rang | Schrift (Google Fonts) | Designer | Lizenz | Reserved Font Name | Ähnlichkeit zu Stay Retro | Hinweise |
| --- | --- | --- | --- | --- | --- | --- |
| **1** | **Leckerli One** | Gesine Todt | OFL 1.1 | "Leckerli" | sehr nah: fette, runde Pinsel-Script, ähnliche Kleinbuchstaben (e, k, S) | 1 Schnitt, TTF ca. 43 KB |
| 2 | Lobster | Impallari Type | OFL 1.1 | "Lobster" | fette, verbundene Retro-Script | sehr verbreitet, wirkt dadurch weniger eigenständig; großer Zeichensatz (TTF ca. 406 KB) |
| 3 | Oleo Script (Bold) | soytutype fonts | OFL 1.1 | "Oleo" | runde, fette Script, etwas ruhiger | Regular und Bold, TTF ca. 35 KB |
| Option | Shrikhand | Jonny Pinhorn | OFL 1.1 | keiner | 70er-Retro, fett-kursiv, nicht verbunden | wirkt eher "Display" als Script |
| Option | Knewave | Tyler Finck | OFL 1.1 | keiner | grober Pinsel, Street-Look | gleicher Mitgestalter wie League Spartan |

Quellen der Lizenzangaben: `METADATA.pb` und `OFL.txt` der jeweiligen Familie im Google-Fonts-Repository. [Q12]

Wichtig bei Schriften **mit** Reserved Font Name (Leckerli One, Lobster, Oleo Script):

- Self-Hosting ist erlaubt. [Q10]
- Reine WOFF2-Kompression ohne Änderung der Fontdaten und Metadaten gilt nicht als Veränderung, Name bleibt erlaubt (OFL-FAQ 2.2.1). [Q10]
- **Subsetting** (Zeichen entfernen) gilt als Veränderung (OFL-FAQ 2.6); dann dürfte die Schrift den reservierten Namen nicht mehr tragen. Praktisch: diese Schriften **nicht subsetten** (Leckerli One ist ohnehin nur ca. 43 KB groß). [Q10]

---

## 5. Datenschutzkonforme Einbindung

### 5.1 Rechtslage

- **LG München I, Urteil vom 20.01.2022, Az. 3 O 17493/20** (GRUR-RS 2022, 612) [Q13]:
  - Die dynamische IP-Adresse ist für den Websitebetreiber ein personenbezogenes Datum (Rn. 5).
  - Die automatische Weitergabe der IP-Adresse an Google beim Laden von Google Fonts ohne Einwilligung war unzulässig (Rn. 7).
  - Kein berechtigtes Interesse, weil Google Fonts auch genutzt werden kann, ohne dass beim Seitenaufruf eine Verbindung zu einem Google-Server hergestellt wird (Rn. 8).
  - Übermittlung in die USA ohne angemessenes Datenschutzniveau (Rn. 12).
  - Folge: Unterlassung, Auskunft, 100 EUR Schadensersatz.
- Seit 10.07.2023 gilt der Angemessenheitsbeschluss zum EU-US Data Privacy Framework (Durchführungsbeschluss (EU) 2023/1795). [Q14] Das betrifft nur den USA-Aspekt (Rn. 12). Das Kernargument (Rn. 8: lokales Hosting ist möglich, also kein berechtigtes Interesse an der Übermittlung) bleibt bestehen.
- Google bestätigt in der eigenen FAQ: Beim Laden über die Google Fonts Web API erhält Google IP-Adresse, angefragte URL und HTTP-Header inklusive User-Agent und Referer. Bei Self-Hosting erhält Google keine Daten über die Websitebesuche. [Q11]

### 5.2 Empfehlung

1. **Alle Schriften selbst hosten** (gleicher Server wie die Website). Keine Requests an `fonts.googleapis.com` oder `fonts.gstatic.com`. Dann ist für Schriften weder Einwilligung noch Cookie-Banner nötig.
2. **Format: nur WOFF2.** W3C-Recommendation [Q15], laut caniuse ca. 97 % Browser-Unterstützung (nicht: Internet Explorer, Opera Mini) [Q16]. Fallback über einen System-Schriften-Stack in `font-family`.
3. **Bezug:** Original-TTF aus dem Google-Fonts-Repository bzw. per Download auf fonts.google.com. Umwandlung in WOFF2 mit einem Werkzeug, das die Fontdaten unverändert komprimiert (z. B. Googles `woff2_compress` oder `fontTools`), Metadaten nicht verändern.
4. **Subsetting:** Pacifico und League Spartan (kein Reserved Font Name) dürfen auf Latin/Latin-Extended reduziert werden. Leckerli One, Lobster, Oleo Script nicht subsetten (Abschnitt 4).
5. **League Spartan als Variable Font** (eine WOFF2-Datei für alle Stärken).
6. **CSS:** `@font-face` mit `font-display: swap`, Überschriften-Schrift per `<link rel="preload" as="font" type="font/woff2" crossorigin>` vorladen.
7. **Lizenzdateien:** je Familie `OFL.txt` neben die Fontdateien legen, z. B. `fonts/leckerli-one/OFL.txt`.
8. **Kontrolle:** im Browser (DevTools, Tab "Netzwerk") prüfen, dass keine Anfragen an Dritt-Server gehen. Auch Vorlagen, Frameworks und Icon-Sets laden manchmal Google Fonts nach.
9. **Datenschutzerklärung:** Bei Self-Hosting entfällt ein Abschnitt zu Google Fonts.

Beispiel:

```css
@font-face {
  font-family: "Leckerli One";
  src: url("/fonts/leckerli-one/LeckerliOne-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "League Spartan";
  src: url("/fonts/league-spartan/LeagueSpartan-Variable.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

h1, h2 { font-family: "Leckerli One", "Segoe Script", cursive; }
body   { font-family: "League Spartan", system-ui, sans-serif; }
```

---

## 6. Entscheidungsbedarf (für #10)

- **Stay Retro kaufen oder ersetzen?** Kauf: 21 USD einmalig, Bindung an eine Domain, Kauf über die Schule nötig. Ersatz durch Leckerli One: kostenlos, ohne Bedingungen außer OFL-Datei. Empfehlung: Leckerli One.
- **Rolle von Pacifico:** als Fließtext ungeeignet; entweder als Überschrift (statt Stay Retro) oder nur für kurze Akzente.

---

## Quellen

- [Q1] dafont, Stay Retro (Lizenzangabe und Autornotiz): https://www.dafont.com/stay-retro.font
- [Q2] dafont, FAQ (Lizenzangabe nur Hinweis): https://www.dafont.com/faq.php
- [Q3] Din Studio, Produktseite Stay Retro (Lizenzstufen, Preise, Dateiformate): https://din-studio.com/product/stay-retro-font/
- [Q4] Din Studio, Lizenzbedingungen: https://din-studio.com/license-2/
- [Q5] Din Studio, FAQ: https://din-studio.com/faq/
- [Q6] Din Studio, Webfont-Anleitung: https://din-studio.com/how-to-use-webfont-on-your-website/
- [Q7] Google Fonts Repository, Pacifico (`METADATA.pb`, `OFL.txt`): https://github.com/google/fonts/tree/main/ofl/pacifico
- [Q8] Google Fonts Repository, League Spartan (`METADATA.pb`, `OFL.txt`): https://github.com/google/fonts/tree/main/ofl/leaguespartan
- [Q9] SIL Open Font License 1.1, offizieller Text: https://openfontlicense.org/open-font-license-official-text/
- [Q10] SIL OFL-FAQ (1.1, 1.10, 2.1, 2.2, 2.2.1, 2.6): https://openfontlicense.org/ofl-faq/
- [Q11] Google Fonts, FAQ (kommerzielle Nutzung, Datenschutz, Self-Hosting): https://fonts.google.com/faq
- [Q12] Google Fonts Repository, Alternativen: https://github.com/google/fonts/tree/main/ofl/leckerlione, https://github.com/google/fonts/tree/main/ofl/lobster, https://github.com/google/fonts/tree/main/ofl/oleoscript, https://github.com/google/fonts/tree/main/ofl/shrikhand, https://github.com/google/fonts/tree/main/ofl/knewave
- [Q13] LG München I, Endurteil vom 20.01.2022, 3 O 17493/20 (Bayern.Recht): https://www.gesetze-bayern.de/Content/Document/Y-300-Z-BECKRS-B-2022-N-612
- [Q14] Durchführungsbeschluss (EU) 2023/1795 (EU-US Data Privacy Framework): https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj?locale=de
- [Q15] W3C, WOFF File Format 2.0 (Recommendation): https://www.w3.org/TR/WOFF2/
- [Q16] caniuse, WOFF 2.0: https://caniuse.com/woff2
