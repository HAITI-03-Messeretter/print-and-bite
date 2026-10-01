# Research: Hosting und Pflege für die Website von PRINT&BITE

- Ticket: [#8](https://github.com/HAITI-03-Messeretter/print-and-bite/issues/8) (Teil der Map #2, blockiert #9)
- Stand: 01.10.2026 (alle Quellen an diesem Tag abgerufen)
- Grundlage: offizielle Doku, Preis-, AGB-, Datenschutz- und AV-Seiten der Anbieter, öffentlich sichtbare Teile von bbs1-lueneburg.de, Handreichung des Kultusministeriums für Schülerfirmen, Research zu #7. Quellen am Ende, im Text als [Qn]. Nicht belegbare Punkte sind als **ungeprüft** markiert.

> **Keine Rechtsberatung.** Datenschutzfragen (Drittland, AV-Vertrag) entscheiden Schulleitung und die oder der Datenschutzbeauftragte der Schule. Rechtliche Pflichtangaben stehen in der Research zu #7 [Q35].

## Kurzantwort

1. **GitHub Pages und Netlify Free scheitern am Setup "privates Repo in einer Organisation auf GitHub Free".** GitHub Pages verlangt dann ein öffentliches Repo [Q1]. Netlify bietet private Org-Repos nur im Pro-Plan (20 USD/Monat) [Q15]. Vercel Hobby ist nicht kommerziell und kann ebenfalls keine privaten Org-Repos [Q26].
2. **Cloudflare Pages funktioniert sofort und kostenlos mit dem privaten Org-Repo** (keine Planbeschränkung dokumentiert, statische Aufrufe unbegrenzt, 500 Builds/Monat) [Q20][Q21]. DPA ist automatisch Vertragsbestandteil, Cloudflare ist aber ein US-Anbieter (EU-US Data Privacy Framework, keine EU-Datenresidenz im Free-Plan) [Q24].
3. **Die Schule hat bereits eine Website** (Joomla 4 oder neuer, erstellt von sketch.media, Server bei Hetzner in Falkenstein) [Q31]. Das Kultusministerium empfiehlt für Schülerfirmen eine **Subdomain der Schul-Homepage** statt eigener Domain [Q33]. Ob die Schule Webspace oder eine Subdomain stellt, ist offen (Fragen in Abschnitt 8).
4. **Pflege durch Laien:** Am besten passt ein **Git-basiertes CMS** auf einer statischen Website. Empfehlung **Sveltia CMS**: kostenlos, läuft komplett im Browser, mobil nutzbar, deutsche Oberfläche, verkleinert Fotos beim Hochladen [Q43]. Preis: Jede Redakteurin und jeder Redakteur braucht ein eigenes GitHub-Konto [Q43][Q12].
5. **Ohne GitHub-Konten** geht es kostenlos nur mit Pages CMS. Die gehostete Version wird aber aus Singapur ohne AV-Vertrag betrieben [Q45], daher nicht empfohlen. WordPress ist für Laien am einfachsten, kostet aber 3 bis 5 EUR/Monat und braucht dauerhaft technische Wartung [Q37][Q38][Q40].
6. **Kontakt:** `mailto:` auf eine Funktionsadresse der Schule plus Telefon (deckt sich mit #7 [Q35]). Formular-Dienste sind meist US-basiert, nutzen oft reCAPTCHA oder haben keinen öffentlichen AV-Vertrag [Q52] bis [Q58].
7. **Domain:** Subdomain der Schule (0 EUR, ein CNAME-Eintrag). Sonst eigene .de-Domain für ca. 5 EUR/Jahr, Inhaber Schule oder Förderverein, nicht eine Schülerin oder ein Schüler persönlich [Q59][Q60].

---

## 1. Ausgangslage und Kriterien

- Kleine Website mit mehreren Seiten (kein Onepager): Unternehmen, Produkte, Termine der Verkaufsaktionen, Fotoarchiv, Kontakt, Impressum, Quiz.
- Budget ca. 0 EUR. DSGVO: Serverstandort, AV-Vertrag nach Art. 28 DSGVO, Drittlandübermittlung.
- Code im **privaten Repo der Organisation `HAITI-03-Messeretter` auf GitHub Free**, vier Entwickler.
- Nach dem Launch pflegen Schülerinnen und Schüler ohne Programmierkenntnisse **Termine** (Datum, Uhrzeit, Ort, Kurztext) und **Archivfotos**.
- Laut #7 ist die Schule (vertreten durch die Schulleitung) Verantwortliche im Datenschutz. Hosting soll bei Schule oder Schulträger liegen, sonst schließt die Schule einen AV-Vertrag [Q35][Q33].

Vergleichskriterien: Kosten, Serverstandort/DSGVO/AV-Vertrag, Pflegeaufwand für Laien, Eignung für das private Org-Repo.

## 2. Vergleich Hosting

| Option | Kosten | Serverstandort / DSGVO / AV-Vertrag | Pflegeaufwand für Laien | Eignung privates Org-Repo (GitHub Free) |
| --- | --- | --- | --- | --- |
| **GitHub Pages** | 0 EUR; Grenzen 1 GB Website, 100 GB/Monat Traffic (weich) [Q3] | US-CDN (Fastly/Cloudflare als Unterauftragnehmer) [Q7]; Besucher-IP wird protokolliert [Q5]; GitHub-DPA gilt nur für Team/Enterprise, **nicht für Free** [Q6]; DPF-zertifiziert [Q7] | über Git-CMS (Abschnitt 3) | **Nein.** Bei GitHub Free muss das Repo öffentlich sein [Q1]. Möglich mit GitHub Team (für Lehrkräfte kostenlos über GitHub Education [Q8]), mit öffentlichem Repo oder mit separatem öffentlichem Deploy-Repo |
| **Netlify Free** | 0 USD, 300 Credits/Monat; Produktions-Deploy 15 Credits, 1 GB Traffic 20 Credits; danach werden **alle Sites pausiert** [Q15][Q16] | US; DPA automatisch über die AGB [Q19]; DPF; Standorte nicht lesbar (**ungeprüft**) | über Git-CMS; Achtung: jede CMS-Speicherung = ein Deploy, also max. ca. 20 Änderungen/Monat | **Nein.** "Private organization repositories" nur im Pro-Plan (20 USD/Monat) [Q15] |
| **Cloudflare Pages** (bzw. Workers Static Assets) | 0 EUR; statische Aufrufe unbegrenzt, 500 Builds/Monat, 20.000 Dateien, 25 MiB/Datei [Q20][Q23] | US-Anbieter mit weltweitem Netz; Daten "primär" in USA und EWR [Q24]; DPA automatisch Teil der Self-Serve-Bedingungen, SCC + DPF [Q24]; EU-Datenlokalisierung nur Enterprise [Q24]; kommerzielle Nutzung erlaubt [Q24] | über Git-CMS; 500 Builds/Monat reichen auch bei vielen CMS-Änderungen | **Ja.** GitHub-App "Cloudflare Workers and Pages" muss eine Org-Ownerin oder ein Org-Owner installieren [Q21]. Alternativ Upload per GitHub Actions |
| Vercel Hobby | 0 USD | US; DPA nur Pro/Enterprise [Q26] | über Git-CMS | **Nein.** Nur "non-commercial personal use", keine privaten Org-Repos [Q26] |
| statichost.eu Hobby | 0 EUR; 1 Site, 10 GB/Monat Traffic, 100 Build-Minuten; Starter 9 EUR/Monat [Q27] | **EU** (Hetzner DE, BunnyWay SI); DPA vorhanden, muss unterschrieben per Mail geschickt werden [Q27] | über Git-CMS | **Ja**, privates Repo per Deploy-Key [Q27]. Kleiner Anbieter, Hobby-Grenzen knapp |
| Codeberg Pages | 0 EUR | **EU** (DE) | über Git-CMS | **Nein.** Repo muss öffentlich auf Codeberg liegen, Inhalte unter freier Lizenz [Q28] |
| **Webspace der Schule** (Server der Schul-Website) | 0 EUR für das Team (ggf. Kosten der Agentur, **ungeprüft**) | **DE** (Hetzner, Falkenstein) [Q31]; AV-Vertrag zwischen Schule und Dienstleister vermutlich vorhanden (**ungeprüft**); MK empfiehlt Subdomain der Schul-Homepage [Q33] | (a) mit SFTP-Zugang: statische Site + Git-CMS; (b) ohne: Bereich im Joomla der Schule, Pflege im Joomla-Backend | **Ja**, wenn SFTP-Zugang: GitHub Actions baut im privaten Repo und lädt hoch (2.000 Actions-Minuten/Monat frei [Q11]). Hängt komplett an der Schule |
| Deutscher Webhoster, statisch per SFTP (netcup, ALL-INKL, STRATO) | netcup Webhosting 1000: 2,69 EUR/Monat (12 Monate) inkl. .de [Q38]; ALL-INKL Privat: 4,95 EUR/Monat inkl. 3 Domains [Q37]; STRATO Starter ab 5 EUR/Monat [Q39] | **DE**; AV-Vertrag im Kundenmenü bzw. automatisch [Q37][Q38][Q39] | über Git-CMS | **Ja**, Deploy per GitHub Actions + SFTP [Q11] |
| WordPress auf deutschem Host | wie Zeile davor (3 bis 5 EUR/Monat) | **DE**, AV-Vertrag wie oben | **gering** für Redaktion (bekannter Editor); **hoch** für Technik: Plugin-/Theme-Updates, Backups, PHP-Versionen, Spam und Login-Schutz [Q40] | Repo nur für das Theme; Git-Workflow und Reviews des Teams greifen für Inhalte nicht |
| WordPress.com Free | 0 USD | Standort für Free nicht angegeben (EU-Rechenzentrum erst im Business-Plan) [Q36]; DPA auf Anfrage auch für Free [Q36] | gering | entfällt (kein Repo); Werbung, keine eigene Domain, keine Plugins [Q36] |

Weitere geprüfte EU-Optionen, die nicht kostenlos sind: Uberspace (DE, "pay what you want", Richtwert 6 bis 12 EUR/Monat, AV-Vertrag im Dashboard) [Q29], bunny.net (SI, ca. 1 USD/Monat Mindestumsatz) [Q30].

### 2.1 GitHub Pages im Detail: was mit GitHub Education möglich ist

- **GitHub Free (Org):** Pages nur aus öffentlichen Repos [Q1]. Pages aus privaten Repos gibt es ab GitHub Pro (Personenkonto), Team und Enterprise. Die Website bleibt trotzdem öffentlich [Q1][Q2].
- **GitHub Team kostenlos für Lehrkräfte:** Lehrkräfte können über GitHub Education kostenlos GitHub Team beantragen. Voraussetzungen: Nachweis als Lehrkraft, verifizierbare Schul-E-Mail-Adresse, persönliches GitHub-Konto [Q8]. Laut Doku kann eine Lehrkraft das auch für eine Schul-AG beantragen [Q8]. Risiko: Laut FAQ werden Anträge bei "non-degree granting institution" abgelehnt. Eine BBS sollte passen, das ist aber **ungeprüft** [Q8]. Wie das Upgrade einer bestehenden Org genau läuft, steht nur in Community-Beiträgen, nicht in der Doku (**ungeprüft**).
- **GitHub Campus Program** (ganze Schule, Enterprise kostenlos): Vertrag durch die Schulleitung, Nutzung nur "non-commercial, academic" und solange kein Gewinn erzielt wird [Q9]. Für eine verkaufende Schülerfirma heikel.
- **Student Developer Pack:** gibt GitHub Pro für das persönliche Konto einer Schülerin oder eines Schülers [Q10]. Das ändert den Plan der Organisation nicht und hilft dem Org-Repo nicht (Ableitung aus [Q2]).
- **Nutzungsbedingungen:** Pages ist nicht für "online business, e-commerce" oder Seiten gedacht, die vor allem kommerziellen Transaktionen dienen [Q4]. Eine reine Infoseite ohne Shop und ohne Preise ist nach unserer Lesart zulässig. Das ist eine Interpretation, keine Aussage von GitHub.
- **Workarounds:** Repo öffentlich machen (dann werden auch Issues öffentlich) oder im privaten Repo bauen und das Ergebnis in ein zweites, öffentliches Repo mit Pages schieben. Das zweite Repo ist keine offizielle Pages-Funktion, sondern Eigenbau mit Deploy-Key.
- **Fazit:** GitHub Pages ist nur sinnvoll, wenn eine Lehrkraft GitHub Team bekommt. Dann gilt auch der GitHub-DPA für Team [Q6]. Ob er bei kostenlosem Education-Team greift, ist **ungeprüft**.

### 2.2 Cloudflare im Detail

- Cloudflare empfiehlt für neue Projekte **Workers** statt Pages. Pages ist aber nicht abgekündigt und weiter "available on all plans" [Q20].
- **Wichtig für die Domain:** Eine **Subdomain mit fremdem DNS** (z. B. `printandbite.bbs1-lueneburg.de`) lässt sich bei **Pages per CNAME** einbinden. Bei **Workers** brauchen Custom Domains eine aktive Cloudflare-Zone, die Domain müsste also mit ihren Nameservern zu Cloudflare umziehen [Q22]. Für eine Schul-Subdomain also **Pages**, nicht Workers.
- Konto: Den DPA schließt Cloudflare mit dem Kontoinhaber [Q24]. Das Konto sollte daher auf eine Funktionsadresse der Schule laufen, nicht auf eine Privatperson aus dem Team.

### 2.3 Schul-Website bbs1-lueneburg.de (nur öffentlich sichtbare Merkmale)

- **CMS: Joomla 4 oder neuer.** Der Generator-Tag ist entfernt, aber typische Pfade sind sichtbar: `/media/system/js/core.min.js`, `/media/vendor/joomla-custom-elements/...`, `joomlaImage://local-images/...`, Template unter `/templates/bbs1/`. Dazu die Editor-Erweiterung JCE Pro und Erweiterungen der Agentur sketch.media (`com_sketchslider_pro`, Cookie `sketchdatesCartCookie`, also offenbar schon eine Termin-Erweiterung) [Q31].
- Impressum: "Website & Programmierung by sketch.media". Hoster ist nicht genannt [Q31]. `www.bbs1-lueneburg.de` zeigt auf eine IP-Adresse von Hetzner (Falkenstein). Die Domain ohne `www` zeigt auf das Netz von LueneCom, dort läuft IServ (`/iserv`) [Q31].
- In der Datenschutzerklärung ist kein Datenschutzbeauftragter namentlich genannt. Bereiche für Schülerfirmen gibt es nicht [Q31].
- Schulträger ist der Landkreis Lüneburg (aus Seiten des Landkreises, nicht von der Schul-Website) [Q32].

## 3. Vergleich Pflege durch Laien (Git-basierte CMS)

Ein Git-CMS ist eine Weboberfläche unter `/admin`. Es speichert Termine und Fotos als Dateien im Repo, danach baut der Hoster die Seite neu. Die Entwickler behalten ihren Git-Workflow, die Redaktion sieht nur Formulare.

| CMS | Kosten | Login der Redaktion | Datenverarbeitung / DSGVO | Laien-UX (Termine, Fotos, Handy) | Reife |
| --- | --- | --- | --- | --- | --- |
| **Sveltia CMS** | 0 EUR, MIT [Q43] | eigenes **GitHub-Konto mit Schreibrecht** pro Person [Q43]; OAuth-Helfer nötig: "Sveltia CMS Authenticator" auf Cloudflare Workers Free [Q44] oder ein anderer Decap-kompatibler OAuth-Client [Q43][Q41] | läuft komplett im Browser, kein CMS-Anbieter dazwischen, "does not collect or store any user data" [Q43]; nur GitHub und der OAuth-Helfer sind beteiligt | **am besten:** voll responsiv, als App installierbar, deutsche Oberfläche, Datumsfeld, Bilder werden beim Upload verkleinert und nach WebP konvertiert, auch HEIC-Handyfotos [Q43] | **Beta** (v0.227, fast tägliche Releases), v1.0 "late 2026" [Q43] |
| Decap CMS (GitHub-Backend) | 0 EUR, MIT [Q41] | GitHub-Konto mit Push-Recht; OAuth über Netlify (braucht Netlify-Projekt) oder eigenen OAuth-Client [Q41] | wie Sveltia | Datumsfeld, deutsche Oberfläche, Bildverkleinerung seit 3.16; **auf dem Handy kaum nutzbar** (Issue seit 2017 offen) [Q41] | stabil (3.16.x, monatliche Releases) [Q41] |
| Decap + Git Gateway / Netlify Identity | 0 USD | Einladung per E-Mail, kein GitHub-Konto | Netlify (US) | wie Decap | **Git Gateway ist abgekündigt** ("deprecated", neue Setups nicht empfohlen) [Q18]; nur auf Netlify, das am privaten Org-Repo scheitert |
| Decap Turbo | Free: nur 1 Platz (Owner); Pro 19 EUR/Monat (bis 15.10.2026 gratis) [Q42] | eigene Turbo-Konten, kein GitHub-Konto | Betreiber in Slowenien, DPA mit SCC, Unterauftragnehmer teils US (Netlify, Cloudflare) [Q42] | wie Decap | Public Preview seit 14.09.2026, nur mit Decap-Beta [Q42] |
| **Pages CMS** (gehostet) | 0 EUR, MIT [Q45] | **Einladung per E-Mail, kein GitHub-Konto nötig** [Q45] | Betreiber "Pages CMS", **Singapur**; Datenschutzerklärung von 2024 ohne DSGVO-Abschnitt, **kein AV-Vertrag**, Serverstandort nicht genannt [Q45]; speichert Login-Daten, Mitarbeitende und Cache [Q45] | mobil optimiert, Datumsfeld, Bildfeld mit mehreren Bildern; **keine Bildverkleinerung** dokumentiert; Upload-Grenze der gehosteten Version vermutet (**ungeprüft**) [Q45] | aktiv, aber faktisch ein einzelner Maintainer [Q45] |
| Pages CMS (selbst gehostet) | 0 EUR Lizenz; Server nötig | wie oben | eigene Kontrolle (EU möglich) | wie oben | braucht Node, PostgreSQL, eigene GitHub-App, SMTP [Q45]: echter Betriebsaufwand |
| TinaCMS (Tina Cloud) | Free: 2 Personen; Team 24 USD/Monat [Q46] | Tina-Cloud-Konten | AWS **USA**, kein DPA gefunden [Q46] | visuelles Editieren; Konfiguration in TypeScript | stabil; Self-Hosting braucht Datenbank und Auth [Q46] |
| Keystatic | Cloud bis 3 Personen frei [Q47] | GitHub-Konto oder Keystatic Cloud | **ungeprüft** | gut | braucht einen **Node-Server** für API-Routen [Q47], passt nicht zu rein statischem Hosting |
| CloudCannon | ab 55 USD/Monat [Q48] | eigene Konten | - | sehr gut | entfällt wegen Kosten |
| Front Matter CMS | 0 EUR [Q48] | VS Code + Git | lokal | nur für Entwickler | entfällt |

GitHub-Details, die alle Git-CMS betreffen:

- Eine Org auf GitHub Free erlaubt beliebig viele Mitglieder bzw. Mitarbeitende in privaten Repos [Q2]. Ein Login darf nur von **einer Person** genutzt werden, Mindestalter 13 Jahre [Q12]. Ein gemeinsames "Redaktions-Konto" für mehrere Personen ist also nicht erlaubt.
- Neue Orgs blockieren fremde OAuth-Apps standardmäßig. Eine OAuth-App, die der Org selbst gehört, ist automatisch zugelassen [Q13]. Die OAuth-App für das CMS daher **unter der Org** anlegen.
- Fotos liegen im Repo. GitHub sperrt Dateien über 100 MiB und empfiehlt Repos unter 1 GB [Q14]. Mit Verkleinerung auf ca. 1600 px als WebP (einige hundert KB pro Foto) reicht das für viele Jahre Archiv.
- Für die Inhalte im Repo gilt bei GitHub Free kein DPA [Q6]. Das passt zur Linie aus #7, im Archiv vor allem Produktfotos ohne erkennbare Personen zu zeigen [Q35].

## 4. Statische Website-Generatoren (kurz)

| Generator | Stärken für dieses Projekt | CMS-Doku |
| --- | --- | --- |
| **Astro** | Content Collections mit Schema (Zod): ein Termin ohne gültiges Datum lässt den Build scheitern, statt eine kaputte Seite zu veröffentlichen; eingebaute Bildoptimierung (WebP/AVIF) für das Archiv [Q49] | Sveltia, Tina [Q43][Q46] |
| Eleventy | sehr einfach, standardmäßig kein JavaScript im Browser, Datendateien in `_data`, offizielles Image-Plugin [Q50] | Sveltia, Tina [Q43][Q46] |
| Hugo | ein einzelnes Programm ohne Node, sehr schnell, Bildverarbeitung eingebaut; Go-Templates sind für Einsteiger sperriger [Q51] | Decap, Sveltia, Tina [Q41][Q43][Q46] |

Alle drei erzeugen reines HTML/CSS/Bilder und laufen damit auf jedem Hoster aus Abschnitt 2. Die Wahl gehört zu #9. Tendenz: Astro, weil die Schema-Prüfung Eingabefehler der Redaktion früh abfängt.

## 5. Kontaktformular ohne eigenes Backend

| Option | Kostenlos | Datenstandort / AV-Vertrag | Spamschutz | Bemerkung |
| --- | --- | --- | --- | --- |
| **`mailto:`-Link** auf Funktionsadresse der Schule + Telefon | ja | kein zusätzlicher Dienst; Postfach z. B. über IServ der Schule (IServ ist laut Bildungsportal ein Auftragsverarbeiter der Schule) [Q34] | Adresse verschleiern | Empfehlung aus #7 [Q35]; braucht ein Mailprogramm beim Besucher |
| Netlify Forms | ja, seit 14.04.2026 ohne Credits [Q16][Q17] | US, DPA über AGB [Q19] | Akismet (Automattic) immer, optional reCAPTCHA [Q17] | **nur auf Netlify**, entfällt damit |
| Formspree | 50 Einsendungen/Monat, laut Anbieter "for testing" [Q52] | AWS USA, kein öffentlicher DPA gefunden [Q52] | eigener Filter + standardmäßig reCAPTCHA [Q52] | nicht empfohlen |
| Web3Forms | 250/Monat (**ungeprüft**, Seite blockiert Abrufe) | USA; Doku sagt "nicht gespeichert", Datenschutzerklärung nennt bis 3 Jahre Speicherung [Q53] | hCaptcha, Honeypot [Q53] | widersprüchlich, nicht empfohlen |
| Basin | 50/Monat, 1 Formular [Q54] | USA/Kanada, DPA nicht öffentlich [Q54] | reCAPTCHA, hCaptcha, Turnstile, Honeypot [Q54] | nicht empfohlen |
| Forminit (früher Getform) | 100/Monat, 1 Formular [Q55] | **ungeprüft** | **ungeprüft** | - |
| Tally (BE) | ja, Formulare und Einsendungen unbegrenzt (Fair Use) [Q56] | Daten in Europa, DPA über AGB, einige Unterauftragnehmer in den USA [Q56] | reCAPTCHA (Google) [Q56] | eingebettetes Fremdformular, Tally-Branding |
| Formbricks (Kiel) | 250 Antworten/Monat [Q57] | Frankfurt, DPA vorhanden; ob er für Free gilt, **ungeprüft** [Q57] | **ungeprüft** | eher Umfrage-Tool als Kontaktformular |
| Form.taxi (AT) | 40/Monat, 3 Formulare [Q58] | gehostet bei ALL-INKL in Dresden [Q58]; AV-Vertrag nicht öffentlich (**ungeprüft**) | "Spam Shield" [Q58] | klassisches HTML-Formular, EU; AV-Vertrag anfragen |
| Eigene Mini-Funktion auf Cloudflare | im Free-Kontingent | Cloudflare (wie Hosting) | selbst gebaut | Absender-Domain muss bei Cloudflare Email Service eingerichtet sein [Q25], also nur mit eigener Domain bei Cloudflare, nicht mit Schul-Subdomain |

reCAPTCHA vermeiden: #7 empfiehlt keine Drittanbieter-Einbindungen beim Seitenaufruf [Q35].

## 6. Domain

| Option | Kosten | Bewertung |
| --- | --- | --- |
| **Subdomain der Schule**, z. B. `printandbite.bbs1-lueneburg.de` | 0 EUR | **Empfehlung des Kultusministeriums** ("am besten über eine Subdomain der Schul-Homepage") [Q33]; zeigt die Zugehörigkeit zur BBS I; Domain gehört dauerhaft der Schule. Technisch nur ein CNAME-Eintrag auf den Hoster (bei Cloudflare nur mit Pages [Q22]). Wer die DNS-Zone verwaltet (Nameserver `dns1.de` bis `dns4.de`), ist **ungeprüft** [Q31] |
| Eigene `.de`-Domain | ca. 5 EUR/Jahr (netcup 0,42 EUR/Monat [Q60]; bei Webhosting-Paketen inklusive [Q37][Q38]) | Inhaberin sollte die Schule oder der Förderverein sein, nicht eine Person aus dem Team. DENIC verlangt keine deutsche Anschrift [Q59]. Ist der Inhaber keine natürliche Person, veröffentlicht DENIC dessen Daten im Whois. Inhaberdaten werden neuerdings verifiziert [Q59] |
| Kostenlose Subdomain des Hosters (`*.pages.dev`, `*.github.io`, `*.netlify.app`) | 0 EUR | gut für Vorschau und Entwicklung, als Dauerlösung unprofessionell und an den Hoster gebunden |
| Domain aus dem GitHub Student Developer Pack (.me, .tech u. a.) | 1 Jahr gratis [Q10] | **nicht empfohlen:** gehört einer Person, danach voller Preis, schlecht bei wechselnden Teams |

## 7. Empfehlung

### 7.1 Architektur (unabhängig vom Hoster)

**Statische Website (Tendenz Astro) im privaten Org-Repo, Termine und Archiv als Dateien mit Schema, Pflege über Sveltia CMS unter `/admin`.**

- Das Ergebnis ist reines HTML/CSS/Bilder. Damit ist der Hoster **austauschbar**, ohne Code oder Inhalte zu ändern. Das ist wichtig, solange die Antwort der Schule aussteht.
- Kaum Angriffsfläche und keine Updates im Betrieb. Das zählt, weil nach dem 18.12.2026 kein IT-Team mehr dauerhaft da ist.
- Jede Änderung der Redaktion ist ein Git-Commit: nachvollziehbar und jederzeit rückgängig zu machen.

### 7.2 Hosting: Reihenfolge je nach Antwort der Schule

1. **Subdomain der Schule + Webspace der Schule per SFTP**, falls die Schule bzw. sketch.media einen Zugang gibt. EU-Server, AV-Vertrag läuft über die Schule, 0 EUR, entspricht der MK-Empfehlung [Q33]. Deploy per GitHub Actions [Q11].
2. **Subdomain der Schule + Cloudflare Pages per CNAME**, falls die Schule keinen Webspace stellt, die oder der Datenschutzbeauftragte aber einen US-Anbieter mit DPA und DPF akzeptiert [Q24]. Funktioniert sofort mit dem privaten Org-Repo [Q21]. Konto auf eine Funktionsadresse der Schule.
3. **Deutscher Webhoster** (netcup ab 2,69 EUR/Monat, ALL-INKL 4,95 EUR/Monat, inkl. .de-Domain und AV-Vertrag) [Q37][Q38], falls EU-Hosting Pflicht ist und die Schule keinen Webspace hat. Kostenlose EU-Alternative mit knappen Grenzen: statichost.eu Hobby [Q27]. Den Vertrag sollte die Schule oder der Förderverein abschließen.

Bis zur Klärung kann das Team auf Cloudflare Pages (`*.pages.dev`) entwickeln und Vorschauen zeigen. Das Ziel lässt sich später ohne Umbau wechseln.

**Nicht empfohlen:**

- **GitHub Pages:** nur mit öffentlichem Repo oder mit GitHub Team über eine Lehrkraft [Q1][Q8]. Wird die Lehrkraft-Variante genehmigt, ist GitHub Pages eine gleichwertige Alternative zu Platz 2.
- **Netlify Free:** keine privaten Org-Repos. 300 Credits reichen für ca. 20 Deploys, danach ist die Site offline [Q15][Q16].
- **Vercel Hobby:** nicht kommerziell, keine privaten Org-Repos [Q26].
- **Codeberg:** Repo muss öffentlich sein [Q28].
- **WordPress.com Free:** Werbung, keine eigene Domain [Q36].

### 7.3 Pflege: Sveltia CMS

Gründe:

- kostenlos, kein zusätzlicher CMS-Anbieter, der Daten verarbeitet
- beste Bedienung auf dem Handy, deutsche Oberfläche
- Fotos werden beim Upload automatisch verkleinert, HEIC-Handyfotos funktionieren
- Doku für Astro, Eleventy und Hugo [Q43]

Trade-offs und Gegenmaßnahmen:

- **Beta-Status:** Version fest einbinden (npm-Paket `@sveltia/cms` selbst ausliefern statt vom CDN UNPKG laden). Das vermeidet auch einen Drittanbieter für die Redaktion [Q43]. Rückfallebene ist Decap CMS mit fast identischer `config.yml` [Q41][Q43].
- **GitHub-Konto pro Person:** zwei bis drei benannte Redakteurinnen und Redakteure mit Schreibrecht nur auf dieses Repo. Beim Jahrgangswechsel werden Zugänge entzogen und neu vergeben, eine kurze Anleitung gehört zur Übergabe. Dafür braucht es eine Zustimmung der Schule (Frage 6).
- **OAuth-Helfer:** Bei Cloudflare-Hosting den Sveltia CMS Authenticator als Worker (Free) [Q44]. Bei Schul- oder deutschem Webspace alternativ ein Decap-kompatibler PHP-OAuth-Client auf demselben Server [Q41], damit kein weiterer Anbieter nötig ist.
- **Ausblick:** Sveltia plant für v1.0 "Commits without a Git service account" [Q43]. Dann bräuchte die Redaktion kein GitHub-Konto mehr. Das ist nicht zugesagt und nicht für den Launch einplanen.

**Wenn die Schule GitHub-Konten für Schülerinnen und Schüler ablehnt:**

- (a) Pages CMS **selbst gehostet** auf EU-Server (Einladung per E-Mail, aber Server, Datenbank und Mailversand müssen betrieben werden) [Q45]
- (b) Decap Turbo Pro für 19 EUR/Monat (EU-Betreiber mit DPA, aber Preview-Status) [Q42]
- (c) WordPress auf deutschem Host, nur wenn eine Lehrkraft oder die Schul-IT die Wartung dauerhaft übernimmt [Q40]
- (d) Termine im bestehenden Joomla der Schule pflegen, dort ist offenbar schon eine Termin-Erweiterung installiert [Q31]

Die **gehostete** Version von Pages CMS (Singapur, kein AV-Vertrag) ist für Daten von Schülerinnen und Schülern nicht zu empfehlen [Q45].

### 7.4 Kontakt und Domain

- **Kontakt:** `mailto:` auf eine Funktionsadresse der Schule plus Telefon des Sekretariats [Q35]. Falls doch ein Formular gewünscht ist: auf dem Schul-Webspace über die Schule. Sonst ein EU-Dienst mit AV-Vertrag (z. B. Form.taxi, AV-Vertrag vorher anfragen) [Q58], ohne reCAPTCHA.
- **Domain:** Subdomain der Schule [Q33]. Falls das nicht geht: eigene .de-Domain auf die Schule oder den Förderverein.

## 8. Fragen an Schule und Schulträger

Ergänzt die Fragenliste aus #7 [Q35] und gehört zu #12.

| Nr. | Frage | an wen |
| --- | --- | --- |
| 1 | Darf die Website unter einer **Subdomain der Schule** laufen (z. B. `printandbite.bbs1-lueneburg.de`)? Wer verwaltet die DNS-Zone von bbs1-lueneburg.de (sketch.media, IT des Landkreises, LueneCom?) und setzt den CNAME-Eintrag? | Schulleitung, Schul-IT |
| 2 | Kann die Schule **Webspace mit SFTP-Zugang** für eine statische Website stellen (z. B. beim Dienstleister der Schul-Website)? Entstehen Kosten, und deckt der bestehende AV-Vertrag das ab? | Schulleitung, sketch.media, Landkreis |
| 3 | Falls kein Webspace: Akzeptiert die oder der **Datenschutzbeauftragte** einen US-Anbieter mit automatischem DPA und EU-US Data Privacy Framework (Cloudflare) für eine öffentliche Infoseite ohne Formular und ohne Tracking? Oder ist EU-Hosting Pflicht? | Datenschutzbeauftragte(r) |
| 4 | Wer schließt Verträge ab und ist **Kontoinhaber** (Hosting-Konto, ggf. Domain, ggf. AV-Vertrag): Schule, Landkreis oder Förderverein? Welche Funktions-E-Mail-Adresse wird dafür genutzt? | Schulleitung |
| 5 | Falls eigene Domain: Wer registriert und bezahlt sie (ca. 5 EUR/Jahr), und wer verlängert sie nach dem Schuljahr? | Schulleitung, Förderverein |
| 6 | Dürfen Schülerinnen und Schüler der Schülerfirma **eigene GitHub-Konten** (US-Anbieter, ab 13 Jahren) nutzen, um Termine und Fotos zu pflegen? Braucht es dafür eine Einwilligung? | Schulleitung, Datenschutzbeauftragte(r) |
| 7 | Wer betreut die Website **nach dem 18.12.2026** technisch (Lehrkraft, nächster IT-Jahrgang)? Wer wird Owner der GitHub-Organisation und des Hosting-Kontos, damit Zugänge beim Jahrgangswechsel übergeben werden können (mindestens zwei Admins)? | Schulleitung, betreuende Lehrkräfte |
| 8 | Würde eine Lehrkraft **GitHub Education** (kostenloses GitHub Team) für die Organisation beantragen? Nur nötig, falls GitHub Pages gewünscht ist. | betreuende Lehrkraft |
| 9 | Gibt es eine **Funktionsadresse** für PRINT&BITE (z. B. über IServ) für den Kontakt, und wer liest sie, auch in den Ferien? | Schulleitung, Schul-IT |
| 10 | Wäre alternativ ein **Bereich auf der Schul-Website** (Joomla) denkbar, etwa für die Termine? | Schulleitung, sketch.media |

## 9. Ungeprüfte Punkte

- Ablauf und Erfolgsaussicht eines GitHub-Education-Antrags für eine BBS; ob der GitHub-DPA bei kostenlosem Education-Team gilt.
- Rechenzentrumsstandorte von Netlify (Trust-Seite nicht lesbar); Speicherort von Netlify-Forms-Daten.
- Wer die DNS-Zone der Schule verwaltet; ob es beim Dienstleister der Schul-Website einen AV-Vertrag und freien Webspace gibt; Joomla-Hauptversion.
- Serverstandort und genaue GitHub-Rechte der gehosteten Pages-CMS-App; Upload-Grenze dort.
- AV-Verträge von Formspree, Form.taxi und Forminit; ob der Formbricks-DPA für den Free-Plan gilt; Web3Forms-Angaben widersprüchlich.
- Mindestpreis Uberspace; Hosting-Standort von Keystatic Cloud.

---

## Quellen

GitHub

- [Q1] GitHub Docs, "Creating a GitHub Pages site": https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- [Q2] GitHub Docs, "GitHub's plans": https://docs.github.com/en/get-started/learning-about-github/githubs-plans
- [Q3] GitHub Docs, "GitHub Pages limits": https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- [Q4] GitHub Terms for Additional Products and Features, Abschnitt Pages: https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#pages
- [Q5] GitHub Docs, "What is GitHub Pages?" (IP-Protokollierung): https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- [Q6] GitHub Customer Terms (Geltungsbereich DPA): https://github.com/customer-terms ; GitHub Data Protection Agreement (Oktober 2025): https://github.com/customer-terms/github-data-protection-agreement
- [Q7] GitHub General Privacy Statement (DPF, SCC; gültig ab 27.04.2026): https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement ; GitHub Subprocessors: https://docs.github.com/en/site-policy/privacy-policies/github-subprocessors
- [Q8] GitHub Education für Lehrkräfte: https://docs.github.com/en/education/about-github-education/github-education-for-teachers/about-github-education-for-teachers ; Antrag: https://docs.github.com/en/education/about-github-education/github-education-for-teachers/apply-to-github-education-as-a-teacher ; Rabattierte Pläne: https://docs.github.com/en/billing/concepts/discounted-plans ; Schul-AGs: https://docs.github.com/en/education/about-github-education/github-education-for-students/about-github-education-for-students ; FAQ: https://education.github.com/teachers
- [Q9] GitHub Campus Program: https://docs.github.com/en/education/about-github-education/use-github-at-your-educational-institution/about-github-campus-program ; Bedingungen: https://github.com/education/schools/terms
- [Q10] GitHub Student Developer Pack: https://education.github.com/pack ; Antrag Schüler: https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student
- [Q11] GitHub Docs, Abrechnung GitHub Actions (2.000 Minuten/Monat für Free-Orgs): https://docs.github.com/en/billing/concepts/product-billing/github-actions
- [Q12] GitHub Terms of Service, Abschnitt B (gültig ab 27.04.2026): https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- [Q13] GitHub Docs, OAuth-App-Zugriffsbeschränkungen: https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions ; GitHub Apps installieren: https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party
- [Q14] GitHub Docs, große Dateien: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github

Netlify

- [Q15] Netlify Pricing: https://www.netlify.com/pricing/ ; Pro vs. Free: https://www.netlify.com/pricing/pro-vs-free/
- [Q16] Netlify Docs, "How credits work" (Stand 12.08.2026): https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/ ; Changelog 14.04.2026: https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/
- [Q17] Netlify Forms, Abrechnung: https://docs.netlify.com/manage/forms/usage-and-billing/ ; Spamfilter: https://docs.netlify.com/manage/forms/spam-filters/ ; Einrichtung: https://docs.netlify.com/manage/forms/setup/
- [Q18] Netlify Git Gateway (Stand 17.09.2026): https://docs.netlify.com/manage/security/secure-access-to-sites/git-gateway/ ; Netlify Identity: https://www.netlify.com/blog/auth0-extension-identity-changes/
- [Q19] Netlify GDPR: https://www.netlify.com/gdpr-ccpa/ ; DPA: https://www.netlify.com/pdf/netlify-dpa.pdf ; Self-Serve Subscription Agreement: https://www.netlify.com/pdf/self-serve-subscription-agreement.pdf

Cloudflare

- [Q20] Cloudflare Pages Übersicht (Stand 25.08.2026): https://developers.cloudflare.com/pages/ ; Limits: https://developers.cloudflare.com/pages/platform/limits/ ; Preise Functions/statische Aufrufe: https://developers.cloudflare.com/pages/functions/pricing/
- [Q21] Cloudflare Pages, GitHub-Integration: https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/
- [Q22] Cloudflare Pages, Custom Domains: https://developers.cloudflare.com/pages/configuration/custom-domains/ ; Workers, Custom Domains: https://developers.cloudflare.com/workers/configuration/routing/custom-domains/
- [Q23] Workers Static Assets, Abrechnung: https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/ ; Workers Preise: https://developers.cloudflare.com/workers/platform/pricing/
- [Q24] Cloudflare Self-Serve Subscription Agreement: https://www.cloudflare.com/terms/ ; Customer DPA (v6.4): https://www.cloudflare.com/cloudflare-customer-dpa/ ; Datenschutzerklärung: https://www.cloudflare.com/privacypolicy/ ; Data Localization Suite: https://developers.cloudflare.com/data-localization/
- [Q25] Cloudflare Email Service, Send Bindings: https://developers.cloudflare.com/email-service/configuration/send-bindings/

Weitere Hoster

- [Q26] Vercel Fair Use: https://vercel.com/docs/limits/fair-use-guidelines ; Hobby und Org-Repos: https://vercel.com/docs/git#using-hobby-teams ; DPA: https://vercel.com/legal/dpa
- [Q27] statichost.eu Preise: https://www.statichost.eu/pricing/ ; DPA: https://www.statichost.eu/dpa/
- [Q28] Codeberg Pages: https://docs.codeberg.org/codeberg-pages/ ; Nutzungsbedingungen: https://codeberg.org/codeberg/org/src/branch/main/TermsOfUse.md
- [Q29] Uberspace: https://uberspace.de/en/product/ ; AV-Vertrag: https://dashboard.uberspace.de/dpa/
- [Q30] bunny.net Preise: https://bunny.net/pricing/ ; DSGVO: https://bunny.net/gdpr/

Schule, Land, Projekt

- [Q31] BBS I Lüneburg, Website (HTML-Quelltext, DNS/RDAP der Domain): https://www.bbs1-lueneburg.de/ ; Impressum: https://www.bbs1-lueneburg.de/impressum.html ; Datenschutz: https://www.bbs1-lueneburg.de/datenschutz.html
- [Q32] Landkreis Lüneburg, berufsbildende Schulen im Landkreis: https://www.landkreis-lueneburg.de/fuer-unsere-buergerinnen-und-buerger/lernen-im-landkreis/schulen-im-landkreis/berufsbildende-schulen-im-landkreis.html
- [Q33] Niedersächsisches Kultusministerium, "Handreichung für Schülerfirmen in Niedersachsen" (Januar 2023), S. 19: https://www.mk.niedersachsen.de/download/193308/Handreichung_Schuelerfirmen_organisiert_wie_richtige_Unternehmen_.pdf
- [Q34] Bildungsportal Niedersachsen, "Häufige Fragen und Antworten zum Datenschutz": https://bildungsportal-niedersachsen.de/schulorganisation/datenschutz-an-schulen/dsgvo-an-schulen-und-studienseminaren/haeufige-fragen-und-antworten-zum-datenschutz
- [Q35] Research zu #7, Rechtliche Pflichtangaben (Branch `research/rechtliche-pflichtangaben`): https://github.com/HAITI-03-Messeretter/print-and-bite/blob/research/rechtliche-pflichtangaben/docs/research/rechtliche-pflichtangaben.md

WordPress

- [Q36] WordPress.com Preise: https://wordpress.com/pricing/ ; Rechenzentrum wählen: https://wordpress.com/support/choose-your-sites-primary-data-center/ ; DPA: https://wordpress.com/support/data-processing-agreements/ ; Plugins: https://wordpress.com/support/plugins/
- [Q37] ALL-INKL Webhosting: https://all-inkl.com/webhosting/ ; Rechenzentrum: https://all-inkl.com/en/about-us/datacenter ; AV-Vertrag: https://all-inkl.com/members/avv_muster_print.php
- [Q38] netcup Webhosting 1000: https://www.netcup.com/de/hosting/webhosting/webhosting-1000-nue ; AV-Vertrag: https://www.netcup.com/en/helpcenter/documentation/general/dpa
- [Q39] STRATO Hosting: https://www.strato.de/hosting/ ; AV-Vertrag FAQ: https://www.strato.de/faq/vertrag/fragen-zur-auftragsverarbeitungsvertrag-avv-und-der-neuen-eu-datenschutzgrundverordnung-dsgvo/
- [Q40] WordPress.org, Auto-Updates für Plugins und Themes: https://wordpress.org/documentation/article/plugins-themes-auto-updates/ ; Core-Updates: https://developer.wordpress.org/advanced-administration/upgrade/upgrading/

CMS

- [Q41] Decap CMS, GitHub-Backend: https://decapcms.org/docs/github-backend/ ; externe OAuth-Clients: https://decapcms.org/docs/external-oauth-clients/ ; Bild-Widget: https://decapcms.org/docs/widgets/image/ ; Mobil-Issue: https://github.com/decaporg/decap-cms/issues/441 ; Releases: https://github.com/decaporg/decap-cms/releases
- [Q42] Decap Turbo: https://decapcms.org/turbo/ ; Abrechnung: https://decapcms.org/docs/turbo-billing/ ; Datenschutz: https://decapcms.org/turbo/privacy/ ; Ankündigung: https://decapcms.org/blog/decap-turbo-public-preview/
- [Q43] Sveltia CMS: https://sveltiacms.app/en/docs/start ; GitHub-Backend: https://sveltiacms.app/en/docs/backends/github ; Architektur: https://sveltiacms.app/en/docs/architecture ; Medien: https://sveltiacms.app/en/docs/media/internal ; Funktionen: https://sveltiacms.app/en/docs/features ; Frameworks: https://sveltiacms.app/en/docs/frameworks ; Roadmap: https://sveltiacms.app/en/docs/roadmap ; FAQ: https://sveltiacms.app/en/docs/faq
- [Q44] Sveltia CMS Authenticator: https://github.com/sveltia/sveltia-cms-auth
- [Q45] Pages CMS: https://pagescms.org/ ; Mitarbeitende: https://pagescms.org/docs/configuration/collaborators/ ; Schnellstart: https://pagescms.org/docs/quick-start/ ; Datenschutz: https://pagescms.org/privacy/ ; AGB: https://pagescms.org/terms/ ; Self-Hosting: https://pagescms.org/docs/guides/installing/self-host/ ; Datenbank: https://pagescms.org/docs/development/database/ ; Upload-Issue: https://github.com/pages-cms/pages-cms/issues/284
- [Q46] TinaCMS Preise: https://tina.io/pricing ; Sicherheit: https://tina.io/security ; Self-Hosting: https://tina.io/docs/self-hosted/overview ; Datenschutz: https://tina.io/privacy-notice
- [Q47] Keystatic GitHub-Modus: https://keystatic.com/docs/github-mode ; Keystatic Cloud: https://keystatic.com/docs/cloud
- [Q48] CloudCannon Preise: https://cloudcannon.com/pricing/ ; Front Matter CMS: https://frontmatter.codes/

Generatoren

- [Q49] Astro Content Collections: https://docs.astro.build/en/guides/content-collections/ ; Bilder: https://docs.astro.build/en/guides/images/
- [Q50] Eleventy: https://www.11ty.dev/docs/ ; globale Daten: https://www.11ty.dev/docs/data-global/ ; Image-Plugin: https://www.11ty.dev/docs/plugins/image/
- [Q51] Hugo: https://gohugo.io/about/introduction/ ; Bildverarbeitung: https://gohugo.io/content-management/image-processing/

Formulardienste

- [Q52] Formspree Pläne: https://formspree.io/plans ; Sicherheit: https://formspree.io/security/
- [Q53] Web3Forms FAQ: https://docs.web3forms.com/getting-started/faq ; Spamschutz: https://docs.web3forms.com/getting-started/customizations/spam-protection ; Datenschutz: https://web3forms.com/privacy
- [Q54] Basin Preise: https://usebasin.com/pricing ; DSGVO: https://usebasin.com/gdpr
- [Q55] Forminit (früher Getform): https://forminit.com/pricing
- [Q56] Tally Preise: https://tally.so/pricing ; DSGVO: https://tally.so/help/gdpr ; reCAPTCHA: https://tally.so/help/recaptcha
- [Q57] Formbricks Preise: https://formbricks.com/pricing ; DPA: https://formbricks.com/dpa
- [Q58] Form.taxi Pläne: https://form.taxi/en/plans ; Datenschutz: https://form.taxi/en/privacy

Domain

- [Q59] DENIC Domainbedingungen: https://www.denic.de/domainbedingungen ; Domainrichtlinien: https://www.denic.de/domainrichtlinien ; FAQ (kein Admin-C seit 2018): https://www.denic.de/en/faq/general-faqs/ ; Inhaberdaten-Verifizierung: https://www.denic.de/en/products/holder-data-verification/
- [Q60] netcup .de-Domain: https://www.netcup.com/de/domain/zusaetzliche-domain-de ; INWX Preisliste: https://www.inwx.de/de/domain/pricelist
