# Research: Rechtliche Pflichtangaben für die Website der Schülerfirma PRINT&BITE

- Ticket: [#7](https://github.com/HAITI-03-Messeretter/print-and-bite/issues/7) (Teil der Map #2, blockiert #9)
- Stand: 01.10.2026 (alle Quellen an diesem Tag abgerufen)
- Grundlage: Gesetzestexte (DDG, MStV, TDDDG, DSGVO, KUG, UStG, NSchG, NDSG, NBGG, VSBG), Handreichung des Niedersächsischen Kultusministeriums für Schülerfirmen, Seiten und Muster von Bildungsportal Niedersachsen / RLSB, NiBiS-Datenschutzportal, Landesbeauftragte für den Datenschutz Niedersachsen (LfD), DSK-Orientierungshilfe, BMF-Schreiben vom 24.10.2025. Quellen am Ende, im Text als [Qn].

> **Keine Rechtsberatung.** Diese Zusammenstellung ist eine Recherche im Rahmen eines Schulprojekts. Sie ersetzt keine rechtliche Prüfung. Verbindlich entscheiden Schulleitung, die oder der Datenschutzbeauftragte der Schule, der Schulträger und die zuständigen Stellen der RLSB. Offene Punkte stehen in Abschnitt 10.

## Kurzantwort

1. **Anbieter ist das Land Niedersachsen, vertreten durch die Schulleitung der BBS I Lüneburg.** Nicht der Schulträger (Landkreis Lüneburg) und nicht die Schülerfirma selbst; die Schülerfirma hat keine eigene Rechtspersönlichkeit. [Q3][Q4]
2. **Impressum ist Pflicht** (§ 5 DDG, § 18 MStV; für öffentliche Stellen der Länder zusätzlich § 24 Abs. 2 MStV). Laut Kultusministerium gehören für Schülerfirmen dazu: Name der Schulleitung, Firmenbezeichnung, **Hinweis auf Schülerfirma als pädagogisches Projekt**, Postanschrift der Schule, E-Mail-Adresse. [Q1][Q2][Q4]
3. **Datenschutzerklärung ist Pflicht** (Art. 13 DSGVO), von jeder Seite erreichbar, mit Kontakt der oder des schulischen Datenschutzbeauftragten. RLSB-Muster existiert. [Q4][Q7][Q8]
4. **Keine Steuerangaben auf der Website.** Insbesondere nicht "Kleinunternehmer nach § 19 UStG": Das Kultusministerium schließt § 19 UStG für Schülerfirmen ausdrücklich aus. Seit dem BMF-Schreiben vom 24.10.2025 können Leistungen schulisch integrierter Schülerfirmen als eng verbundene Umsätze nach § 4 Nr. 21 UStG steuerfrei sein; Klärung im Einzelfall über den Fachbereich Umsatzbesteuerung der RLSB Osnabrück. [Q4][Q9][Q10]
5. **Haftung trägt grundsätzlich das Land.** Ein "Haftungsausschluss" ist dafür nicht nötig; wichtig ist, keine echte Rechtsform vorzutäuschen (eine "Schüler-GmbH" ist nur eine Simulation). [Q4]
6. **Keine Drittanbieter ohne Einwilligung:** Schriften selbst hosten, Karte als statisches Bild mit Link statt eingebetteter Karte, Videos selbst hosten oder nur per Zwei-Klick, keine Analyse-Tools. Dann ist kein Cookie-Banner nötig. [Q17][Q18][Q20][Q7]
7. **Kontaktweg:** `mailto:` auf eine funktionale Adresse in der Schul-Domain plus Telefonnummer der Schule. Ein Kontaktformular ist zulässig, bringt aber Zusatzpflichten (TLS, Datenschutz-Abschnitt, ggf. Auftragsverarbeitung). [Q1][Q4][Q19][Q22]
8. **Fotos von Personen nur mit ausdrücklicher Einwilligung für die Website.** Laut LfD ist bei schulischen Pflichtveranstaltungen in der Regel keine freiwillige Einwilligung möglich. Für die Website daher bevorzugt **Produktfotos ohne erkennbare Personen**. [Q14][Q15]
9. **Barrierefreiheit:** Die strengen Vorgaben des NBGG (§§ 9a bis 9e, inkl. Erklärung zur Barrierefreiheit) gelten für Schul-Websites nicht; barrierearm bauen ist trotzdem sinnvoll. [Q26]
10. **Entfällt:** Link zur EU-OS-Plattform (Verordnung seit 20.07.2025 aufgehoben), Preisangaben (keine Preise auf der Website), Handelsregister (keine Eintragung). [Q25]

---

## 1. Wer ist wofür verantwortlich?

| Rolle | Wer | Quelle |
| --- | --- | --- |
| Diensteanbieter (Impressum) | **Land Niedersachsen, vertreten durch die Schulleitung** | NiBiS: "Diensteanbieter im Sinne des DDG: Land Niedersachsen, vertreten durch Schulleitung", ausdrücklich nicht der Schulträger [Q3] |
| Verantwortlicher im Datenschutz | die Schule (BBS I Lüneburg), vertreten durch die Schulleitung | RLSB-Muster nennt die Schule als Verantwortliche, "Vertretungsberechtigt: Schulleiter" [Q8]; Schulleitung verantwortlich für Datenschutz nach § 43 Abs. 2 Satz 2 NSchG [Q5][Q7] |
| Verkäufer, Haftung, Gewährleistung | Land Niedersachsen ("Schülerfirma als pädagogisches Projekt des Landes") | MK-Handreichung S. 14 f. [Q4] |
| Steuerpflichtiger | Land Niedersachsen, zentrale Steuererklärung aller öffentlichen Schulen über RLSB Osnabrück | MK-Handreichung S. 12 [Q4]; Bildungsportal [Q9] |
| Schulträger (Landkreis Lüneburg) | Zustimmung zur Gründung, stellt Sachmittel; ggf. IT/Hosting | MK-Handreichung S. 1 [Q4]; Schulträger berufsbildender Schulen sind die Landkreise und kreisfreien Städte, § 102 NSchG [Q6] |
| Schülerfirma PRINT&BITE | kein eigenes Rechtssubjekt; Rechtsform (z. B. Schüler-GmbH) ist "immer nur eine Simulation", die "in der Außenwirkung jedoch keinerlei rechtswirksame Bedeutung hat" | MK-Handreichung S. 5 [Q4] |
| Projektverantwortung | "in letzter Konsequenz die Schulleiterin bzw. der Schulleiter" | MK-Handreichung S. 5 [Q4] |

Voraussetzung für diese Zuordnung (und für Versicherungsschutz): PRINT&BITE ist von der Schulleitung genehmigt, der Schulträger hat zugestimmt, Schulvorstand, Gesamtkonferenz und Erziehungsberechtigte sind informiert, und es gibt eine schriftliche Kooperationsvereinbarung (Muster: Anlage 1 der Handreichung), die u. a. die **Vertriebswege** (also auch die Website) und den Hinweis auf Datenschutz und Urheberrecht enthält. [Q4, S. 1 f.]

Die Handreichung empfiehlt außerdem: Homepage der Schülerfirma "am besten über eine **Subdomain der Schul-Homepage**", keine eigene Domain, und eine eigene E-Mail-Adresse "in der für die Schule gebräuchlichen Form". So liegen die rechtlichen Bestimmungen in der Verantwortung der Schule. [Q4, S. 19]

---

## 2. Impressum

### 2.1 Rechtsgrundlagen

- **§ 5 Abs. 1 DDG** gilt für "geschäftsmäßige, in der Regel gegen Entgelt angebotene digitale Dienste". Die Website bewirbt den Verkauf von Produkten; das spricht für Geschäftsmäßigkeit. Die Angaben müssen "leicht erkennbar und unmittelbar erreichbar" sein und "ständig verfügbar" gehalten werden. [Q1]
- **§ 24 Abs. 2 MStV**: Für die öffentlichen Stellen der Länder gelten die Bestimmungen des DDG entsprechend. Die Impressumspflicht greift also auch dann, wenn man die Geschäftsmäßigkeit bezweifeln würde. [Q2]
- **§ 18 Abs. 1 MStV**: Name und Anschrift, bei juristischen Personen auch Name und Anschrift des Vertretungsberechtigten. [Q2]
- **§ 18 Abs. 2 MStV**: Nur bei **journalistisch-redaktionell gestalteten** Angeboten (z. B. ein regelmäßig gepflegter News-/Blog-Bereich) ist zusätzlich ein Verantwortlicher mit Name und Anschrift zu benennen. Diese Person muss u. a. ihren ständigen Aufenthalt im Inland haben und **unbeschränkt geschäftsfähig** sein. Die Ausnahme für Jugendliche gilt nur für Angebote, "die für Jugendliche bestimmt sind" - das ist bei einer Verkaufs-Website für alle nicht der Fall. Also: wenn überhaupt, die **betreuende Lehrkraft** benennen, keine minderjährigen Schülerinnen oder Schüler. [Q2]
- Hinweis: Die MK-Handreichung (Januar 2023) nennt noch "§ 5 des Telemediengesetzes bzw. § 55 Rundfunkstaatsvertrag". Beide sind abgelöst; heute gelten § 5 DDG und § 18 MStV. [Q4][Q1][Q2]

### 2.2 Checkliste Impressum

| Angabe | Pflicht? | Grundlage | Inhalt für PRINT&BITE |
| --- | --- | --- | --- |
| Name und Anschrift des Anbieters | ja | § 5 Abs. 1 Nr. 1 DDG, § 18 Abs. 1 MStV | Land Niedersachsen; Berufsbildende Schulen I Lüneburg, Spillbrunnenweg 1, 21337 Lüneburg |
| Rechtsform | ja bei juristischen Personen | § 5 Abs. 1 Nr. 1 DDG | im NiBiS-Muster nicht ausgeschrieben; vorsichtshalber "(juristische Person des öffentlichen Rechts)" ergänzen |
| Vertretungsberechtigter | ja | § 5 Abs. 1 Nr. 1 DDG, § 18 Abs. 1 Nr. 2 MStV | Schulleitung mit **vollständigem Namen** (MK-Handreichung) [Q4] |
| E-Mail-Adresse | ja | § 5 Abs. 1 Nr. 2 DDG | funktionale Adresse in der Schul-Domain (siehe Abschnitt 5) |
| zweiter schneller Kontaktweg | ja | § 5 Abs. 1 Nr. 2 DDG; EuGH C-298/07: neben E-Mail ein weiterer schneller, unmittelbarer Weg, z. B. Telefon oder elektronisches Anfrageformular [Q22] | Telefonnummer des Sekretariats |
| Firmenbezeichnung | ja (MK) | MK-Handreichung S. 20 [Q4] | PRINT&BITE |
| Hinweis Schülerfirma als pädagogisches Projekt | ja (MK) | MK-Handreichung S. 20 [Q4] | siehe Formulierung in 3.4 |
| Kontakt Datenschutzbeauftragte(r) | in der DSE Pflicht, im Impressum empfohlen | Art. 13 Abs. 1 lit. b, Art. 37 Abs. 7 DSGVO [Q12]; NiBiS empfiehlt das Impressum als Ort [Q21] | funktionale Adresse, z. B. datenschutz@... der Schule |
| Verantwortlicher nach § 18 Abs. 2 MStV | nur bei journalistisch-redaktionellem Teil | § 18 Abs. 2 MStV [Q2] | betreuende Lehrkraft (volljährig) |
| Handelsregister | entfällt | § 5 Abs. 1 Nr. 4 DDG | keine Eintragung, **nichts erfinden** |
| USt-IdNr. / W-IdNr. | nur falls vorhanden | § 5 Abs. 1 Nr. 6 DDG | offene Frage an RLSB Osnabrück (Abschnitt 10) |
| Aufsichtsbehörde für zulassungspflichtige Tätigkeit | entfällt | § 5 Abs. 1 Nr. 3 DDG | keine Zulassung nötig |
| Verbraucherschlichtung | unklar | § 36 VSBG: gilt für "Unternehmer", die eine Webseite unterhalten; Ausnahme nur bei höchstens zehn Beschäftigten [Q24] | offene Frage (Abschnitt 10); gängiger Satz siehe Muster |
| Link zur EU-OS-Plattform | **entfällt** | Verordnung (EU) Nr. 524/2013 mit Wirkung zum 20.07.2025 durch Verordnung (EU) 2024/3228 aufgehoben [Q25] | nicht aus alten Vorlagen übernehmen |
| Erreichbarkeit | ja | § 5 Abs. 1 DDG; BGH I ZR 228/03: Erreichbarkeit über zwei Klicks mit verständlichem Linktext ("Kontakt", "Impressum") genügt [Q23] | Link "Impressum" im Footer jeder Seite |

### 2.3 Textbaustein Impressum (Entwurf)

Werte in eckigen Klammern sind von der Schule zu bestätigen. Name und Telefonnummer stammen aus dem Impressum der Schul-Website, Stand 01.10.2026 [Q30].

```text
Impressum

PRINT&BITE - Schülerfirma der Berufsbildenden Schulen I Lüneburg
PRINT&BITE ist ein pädagogisches Schulprojekt der BBS I Lüneburg und
kein eigenständiges Unternehmen.

Diensteanbieter im Sinne des DDG
Land Niedersachsen (juristische Person des öffentlichen Rechts)
vertreten durch die Schulleitung der Berufsbildenden Schulen I Lüneburg:
[Oberstudiendirektor Heiko Lüdemann]

Berufsbildende Schulen I Lüneburg
Spillbrunnenweg 1
21337 Lüneburg
Telefon: [04131 99 220 600]
E-Mail: [printandbite@bbs1-lueneburg.de]  (Platzhalter, Adresse anzulegen)

Datenschutzbeauftragte(r) der Schule: [datenschutz@bbs1-lueneburg.de]

[Nur falls ein News-/Blog-Bereich entsteht:]
Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV:
[Name der betreuenden Lehrkraft], Anschrift wie oben

[Falls nach Klärung nötig, siehe offene Punkte:]
Verbraucherstreitbeilegung: Wir sind nicht bereit und nicht verpflichtet,
an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle
teilzunehmen.
```

---

## 3. Hinweis "Schülerunternehmen": Status, Haftung, Steuern

### 3.1 Begriff

"Formal korrekt" ist laut Kultusministerium "Schülerunternehmen"; in Niedersachsen hat sich "Schülerfirma" durchgesetzt, beide werden synonym verwendet. [Q4, S. 5] Beide Begriffe sind auf der Website möglich.

### 3.2 Haftung und Versicherung

- Sachmängel, Produkthaftung und deliktische Haftung treffen grundsätzlich **das Land Niedersachsen**; das Land kann die Schulleitung in Regress nehmen. Bei vorsätzlich oder grob fahrlässig verursachten Schäden haften Schülerinnen und Schüler bzw. Erziehungsberechtigte persönlich. [Q4, S. 14 f.]
- Unfallversicherung über den Gemeinde-Unfallversicherungsverband (GUV), Schäden über den Kommunalen Schadenausgleich (KSA), jeweils **nur als von der Schulleitung anerkanntes Schulprojekt**. [Q4, S. 17]
- Für die Website heißt das: kein eigener "Haftungsausschluss" nötig oder wirksam, um die Haftung zu verschieben. Die Handreichung empfiehlt einen Hinweis zum Haftungsausschluss für externe Links [Q4, S. 20]; wichtiger ist, verlinkte Seiten **vor dem Verlinken** auf Rechtmäßigkeit zu prüfen und das Datum zu notieren [Q28]. Für Inhalte auf der Schul-Website (z. B. Urheberrechtsverletzungen bei Bildern) haftet laut OLG Celle (13 U 95/15) das Land, nicht die einzelne Lehrkraft. [Q28]
- Simulierte Rechtsformen nur erkennbar als Simulation zeigen (z. B. "Schüler-GmbH"), nie "GmbH" allein. [Q4, S. 5]

### 3.3 Umsatzsteuer

| Zeitpunkt | Rechtslage | Quelle |
| --- | --- | --- |
| MK-Handreichung (Januar 2023) | bis Ende 2024 Übergangsregelung, Umsatzsteuer erst oberhalb einer Geringfügigkeitsgrenze von 45.000 Euro; danach grundsätzlich steuerpflichtig nach § 2 Abs. 1 i. V. m. § 2b UStG; Leistungen dem Land zuzurechnen; **"Die sogenannte Kleinunternehmerregelung (§19 UStG) wird keine Anwendung finden"**, da auf die Umsätze aller Landesdienststellen abzustellen ist | MK-Handreichung S. 12 [Q4] |
| Jahressteuergesetz 2024 (Stand Bildungsportal 2026) | Übergangsregelung für das Land um zwei Jahre bis 31.12.2026 verlängert, Umsätze nach alter Rechtslage; schulrelevante Neuregelung nach § 2b UStG frühestens ab 01.01.2027 | Bildungsportal [Q9] |
| BMF-Schreiben 24.10.2025 | Zu den nach § 4 Nr. 21 UStG steuerfreien "eng verbundenen Umsätzen" können gehören: "Leistungen von Schülerfirmen und Schülergenossenschaften, die rechtlich unselbständig, in die Organisationsstruktur der Schule integriert sind und in denen im Rahmen von unternehmerischen Schulprojekten ökonomisches Handeln gelehrt oder berufliche Orientierung vertieft wird" (UStAE 4.21.1 Abs. 16 Nr. 4). Bedingung (Abs. 15): u. a. "nicht im Wesentlichen dazu bestimmt", zusätzliche Einnahmen in unmittelbarem Wettbewerb zu gewerblichen Unternehmen zu erzielen. | BMF [Q10]; § 4 Nr. 21 UStG [Q11] |

Folgen für die Website:

- **Keine Umsatzsteuer-Hinweise** auf der Website. Es werden keine Preise gezeigt und keine Verträge online geschlossen; ein Steuerhinweis ist dafür nicht erforderlich.
- **Nie** "umsatzsteuerbefreit nach § 19 UStG (Kleinunternehmer)" schreiben; das widerspricht der Aussage des Kultusministeriums. [Q4]
- Die Anforderung "Hinweis auf Schülerunternehmen aus Gründen wie Haftung, Mehrwertsteuerbefreiung" wird durch den **Status-Hinweis** erfüllt (3.4): Er macht erkennbar, dass ein schulisch integriertes, pädagogisches Projekt handelt. Genau darauf stellen sowohl die Haftungszuordnung (Land) als auch die Steuerbefreiung nach BMF ab.
- Ob die konkreten Umsätze (3D-Druck, Holzprodukte, Snacks am Stand) unter § 4 Nr. 21 UStG fallen, entscheidet nicht die Website, sondern die Klärung mit dem Fachbereich Umsatzbesteuerung der RLSB Osnabrück (offener Punkt).

### 3.4 Formulierungsvorschläge

Footer (jede Seite, kurz):

```text
PRINT&BITE ist eine Schülerfirma der Berufsbildenden Schulen I Lüneburg - ein pädagogisches Schulprojekt.
Impressum · Datenschutz
```

Seite "Über uns" bzw. Impressum (lang):

```text
PRINT&BITE ist eine Schülerfirma (Schülerunternehmen) der Berufsbildenden
Schulen I Lüneburg. Sie ist ein von der Schulleitung genehmigtes
pädagogisches Schulprojekt ohne eigene Rechtspersönlichkeit. Träger der
Schülerfirma ist die Schule; Anbieter dieser Website ist das Land
Niedersachsen, vertreten durch die Schulleitung der BBS I Lüneburg.
```

Optional (nicht rechtlich nötig, beugt Missverständnissen vor): "Kein Online-Shop: Unsere Produkte gibt es an unseren Verkaufsständen."

---

## 4. Datenschutzerklärung

### 4.1 Grundlagen

- Pflicht zur Information nach Art. 13 DSGVO, in klarer und einfacher Sprache (Art. 12 Abs. 1). [Q12][Q19]
- Die Datenschutzerklärung muss "von jeder untergeordneten Seite aus erreichbar sein". [Q4, S. 20]
- Bildungsportal-FAQ: Die Schulhomepage muss Impressum und Datenschutzerklärung enthalten. [Q7]
- RLSB-Muster "Datenschutzerklärung Schulhomepage" (Stand 01.12.2020) als Ausgangspunkt; Abschnitte zu Logfiles, Cookies und Kontakt sind individuell anzupassen. Bei Analyse-Tools, Social-Media-Plugins, Google Fonts oder Google reCAPTCHA soll Rücksprache mit dem Datenschutzdezernat der RLSB gehalten werden. [Q8]
- Öffentliche Stellen müssen eine(n) Datenschutzbeauftragte(n) benennen, Kontaktdaten veröffentlichen und der LfD melden (Art. 37 Abs. 1 lit. a, Abs. 7 DSGVO). [Q7][Q4, S. 9]

### 4.2 Checkliste Pflichtinhalte (Art. 13 DSGVO)

- [ ] Name und Kontaktdaten des Verantwortlichen: BBS I Lüneburg, vertreten durch die Schulleitung (Art. 13 Abs. 1 lit. a)
- [ ] Kontaktdaten der oder des Datenschutzbeauftragten (Art. 13 Abs. 1 lit. b)
- [ ] Zwecke und Rechtsgrundlagen je Verarbeitung (Art. 13 Abs. 1 lit. c): Bereitstellung/Logfiles, E-Mail-Kontakt, ggf. Formular, ggf. Fotos
- [ ] Empfänger: Hosting-Dienstleister als Auftragsverarbeiter (Art. 13 Abs. 1 lit. e, Art. 28)
- [ ] Drittlandübermittlung, falls ein Dienst außerhalb der EU beteiligt ist (Art. 13 Abs. 1 lit. f)
- [ ] Speicherdauer, z. B. Logfiles; das RLSB-Muster hält mehr als zwei Monate "nicht für vertretbar" (Art. 13 Abs. 2 lit. a) [Q8]
- [ ] Betroffenenrechte: Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch, Datenübertragbarkeit (Art. 15 bis 21)
- [ ] Widerruf erteilter Einwilligungen (Art. 7 Abs. 3)
- [ ] Beschwerderecht bei der Aufsichtsbehörde: Die Landesbeauftragte für den Datenschutz Niedersachsen, Prinzenstraße 5, 30159 Hannover, poststelle@lfd.niedersachsen.de (Art. 77) [Q8]
- [ ] Cookies: "Wir verwenden keine Cookies" (wenn zutreffend; Variante im RLSB-Muster) [Q8]

### 4.3 Achtung bei der Rechtsgrundlage

- Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse) "gilt nicht für die von Behörden in Erfüllung ihrer Aufgaben vorgenommene Verarbeitung" (Art. 6 Abs. 1 Unterabs. 2). Die LfD wendet das ausdrücklich auf Schulen an. [Q12][Q14]
- Das RLSB-Muster stützt Logfiles und technische Cookies trotzdem auf lit. f. [Q8] Für eine öffentliche Stelle naheliegender ist Art. 6 Abs. 1 lit. e i. V. m. § 3 NDSG (Verarbeitung zur Aufgabenerfüllung) [Q13][Q18, Rn. 106]. Das sollte die oder der Datenschutzbeauftragte festlegen (offener Punkt).
- Fotos von Personen: nur Einwilligung, § 3 NDSG greift dafür nicht. [Q14]
- Die Datenschutzerklärung der Schul-Website nicht ungeprüft übernehmen: Sie nennt z. B. Google Webfonts [Q30]; für PRINT&BITE sollen Schriften lokal eingebunden werden (Abschnitt 7).

---

## 5. Kontaktweg: Formular oder mailto

| Kriterium | `mailto:`-Link | Kontaktformular |
| --- | --- | --- |
| Erfüllt § 5 DDG (E-Mail-Adresse muss genannt sein) | ja | nein, die E-Mail-Adresse muss trotzdem im Impressum stehen [Q1][Q22] |
| Technik | keine; funktioniert auf statischem Hosting | braucht Server-Logik oder externen Formulardienst |
| Verschlüsselung | Transport liegt beim Mailsystem der Schule | Übertragung per HTTPS/TLS nach Stand der Technik nötig (§ 19 Abs. 4 Satz 3 TDDDG; LfD) [Q17][Q19] |
| Datenschutzerklärung | Abschnitt "Kontakt per E-Mail" (RLSB-Muster Nr. V) [Q8] | zusätzlicher Abschnitt mit Feldern, Zweck, Löschung [Q8]; bei externem Dienst Auftragsverarbeitung (Art. 28) [Q19] |
| Spam-Schutz | Adresse kann gesammelt werden | Honeypot o. ä.; **kein Google reCAPTCHA** ohne Rücksprache mit der RLSB [Q8] |
| Cookie-/Einwilligungsfrage | keine | keine, solange kein Drittanbieter-Skript geladen wird [Q17][Q18, Rn. 76] |

Empfehlung: **`mailto:` auf eine funktionale Adresse der Schulform** (MK: "eigene E-Mail-Adresse in der für die Schule gebräuchlichen Form") **plus Telefonnummer des Sekretariats** als zweiter schneller Kontaktweg. [Q4, S. 19][Q22] Das Postfach muss auch in unterrichtsfreien Zeiten kontrolliert werden. [Q4, S. 20] Falls doch ein Formular gewünscht ist: nur Pflichtfelder E-Mail und Nachricht, Hosting bei der Schule bzw. beim Schulträger, TLS, Abschnitt in der Datenschutzerklärung.

---

## 6. Fotos von (minderjährigen) Schülerinnen und Schülern

Rechtslage:

- Öffentliche Stellen können Personenfotos für die Öffentlichkeitsarbeit **nur auf eine Einwilligung** stützen (Art. 6 Abs. 1 lit. a, Art. 7 DSGVO); lit. f und § 3 NDSG scheiden aus. [Q14]
- Die Einwilligung muss **freiwillig** sein. LfD: "In Zusammenhang mit schulischen Pflichtveranstaltungen kann in der Regel keine freiwillige Einwilligung erteilt werden." Möglich ist sie z. B. bei Fotos auf der Schulwebseite außerhalb von Pflichtteilnahmen. [Q14]
- Für die Veröffentlichung auf der Website ist eine **explizite Einwilligung** nötig; eine allgemeine Foto-Einwilligung, die nicht zwischen Print und online unterscheidet, reicht nicht. [Q14]
- Schülerfotos **nicht in sozialen Netzwerken** veröffentlichen (Kontrollverlust, Nutzungsrechte der Plattformen). [Q14]
- KUG: Bildnisse dürfen "nur mit Einwilligung des Abgebildeten verbreitet oder öffentlich zur Schau gestellt werden" (§ 22); die Ausnahmen in § 23 (z. B. Personen als Beiwerk) sind eng. [Q16]
- Minderjährige: Einwilligung der Erziehungsberechtigten; zusätzlich die des Kindes ab 14 Jahren (NiBiS) bzw. "i.d.R. ab der Vollendung des 15. Lebensjahres" (Bildungsportal-FAQ). Pragmatisch: **ab 14 Jahren beide**. Volljährige Schülerinnen und Schüler (an einer BBS häufig) willigen selbst ein. [Q15][Q7]
- Schriftlich einholen (Nachweispflicht), Zweck und Medium genau benennen, Namen zum Foto nur mit eigener Einwilligung, Hinweis "Diese Einwilligung ist freiwillig. Bei Nichterteilung entstehen Ihnen bzw. Ihrem Kind keine Nachteile." [Q15]
- Widerruf jederzeit mit Wirkung für die Zukunft (Art. 7 Abs. 3 DSGVO); Foto dann von der Website entfernen. [Q15][Q12]
- Lehrkräfte: Einwilligung nach § 88 NBG i. V. m. Art. 6 Abs. 1 lit. a DSGVO, Freiwilligkeit im Dienstverhältnis besonders prüfen. [Q14]
- Fremde Bilder (Stock, Fotografen, Internet) nur mit geklärten Nutzungsrechten. [Q28][Q29]

Folgen für Mockups und Website:

- Bildsprache auf **Produkte, Hände, Werkzeuge, 3D-Drucker, Holz, Stand ohne erkennbare Gesichter** ausrichten.
- Team-Seite nur mit Einwilligungen; Alternative ohne Fotos: Vornamen oder Funktionen, Illustrationen.
- Platzhalter in Mockups so wählen, dass die Seite auch **ganz ohne Personenfotos** funktioniert (Widerruf darf kein Layout zerstören).

---

## 7. Eingebettete Karten, Videos, Schriften und andere Drittinhalte

Grundsatz: Wer Inhalte von fremden Servern lädt (Schriften, Skripte, Stadtpläne, Videos, Social-Media-Inhalte), legt personenbezogene Daten (mindestens die IP-Adresse) gegenüber dem Drittanbieter offen und braucht dafür eine Rechtsgrundlage. [Q18, Rn. 101] Zusatzdienste wie Kartendienste gelten nicht automatisch als vom Nutzer "ausdrücklich gewünscht", nur weil er die Seite aufruft. [Q18, Rn. 76] Werden dabei Informationen im Endgerät gespeichert oder ausgelesen, ist nach § 25 TDDDG eine Einwilligung nötig, außer es ist für den ausdrücklich gewünschten Dienst unbedingt erforderlich. [Q17] Bildungsportal-FAQ: Wenn eine Einwilligung technisch nicht korrekt umsetzbar ist, auf einwilligungsbedürftige Cookies verzichten. [Q7]

| Element | Empfehlung | Begründung |
| --- | --- | --- |
| Schriften | **selbst hosten** (gleiche Domain), keine Einbindung über Google-Server | LfD empfiehlt lokale Einbindung; LG München I, 20.01.2022, 3 O 17493/20 (100 Euro Schadensersatz bei Online-Einbindung) [Q20]; Bildungsportal-FAQ [Q7]. Lizenzfragen: siehe [Q32] |
| Karte / Anfahrt | **statisches Kartenbild** (selbst gehostet) plus Adresse als Text und Link "Route in OpenStreetMap öffnen" | kein Datenabfluss beim Seitenaufruf; OSM-Daten verlangen die Quellenangabe "© OpenStreetMap contributors" (ODbL) [Q27]; Weiterleitung zu anderem Anbieter kenntlich machen (§ 19 Abs. 3 TDDDG) [Q17] |
| Eingebettete Karte (Google Maps, OSM-iframe) | nur nach Einwilligung (Zwei-Klick-Lösung) | Drittinhalt [Q18, Rn. 76, 101] |
| Videos | **selbst hosten** (MP4/WebM) | kein Drittanbieter |
| YouTube/Vimeo | nur Zwei-Klick mit Einwilligung, auch im "nocookie"-Modus | Drittinhalt [Q18, Rn. 101] |
| Social Media | **einfache Links** (Text oder eigenes Icon), keine Plugins/Feeds | gemeinsame Verantwortlichkeit bei Plugins (EuGH "Fashion ID", Darstellung NiBiS) [Q29]; LfD rät von Schülerfotos in sozialen Netzwerken ab [Q14] |
| CSS/JS-Bibliotheken | selbst hosten, kein CDN | "Skripte" sind Drittinhalte [Q18, Rn. 101] |
| Analyse/Statistik | weglassen; falls später gewünscht, vorher mit RLSB-Datenschutzdezernat klären | RLSB-Muster [Q8] |
| Hosting | bei Schule/Schulträger bzw. Subdomain der Schul-Website; sonst Auftragsverarbeitungsvertrag (Art. 28) durch die Schule | MK [Q4, S. 19]; LfD [Q19]; Bildungsportal-Muster AV-Vertrag [Q7] |

Ergebnis: Mit diesen Entscheidungen setzt die Website keine einwilligungsbedürftigen Cookies und lädt nichts von Dritten; **ein Cookie-Banner entfällt**. Sobald ein Element mit Einwilligung (Karte, YouTube) dazukommt, braucht es eine Zwei-Klick-Lösung oder ein Consent-Tool, das den Anforderungen der LfD genügt. [Q19]

---

## 8. Weitere Punkte

- **Barrierefreiheit:** Nach § 9 Abs. 2 Satz 1 NBGG gelten die §§ 9a bis 9e (barrierefreie Gestaltung, Erklärung zur Barrierefreiheit, Feedback, Durchsetzung) **nicht** für Websites "von Schulen ... in Trägerschaft öffentlicher Stellen, mit Ausnahme der Inhalte, die sich auf wesentliche Online-Verwaltungsfunktionen beziehen"; nach § 9 Abs. 3 gilt § 9 in der bis 01.11.2018 geltenden Fassung weiter. [Q26] Eine Erklärung zur Barrierefreiheit ist damit nicht Pflicht. Die Schul-Website hat trotzdem eine. [Q30] Empfehlung: barrierearm bauen (Kontraste, Alternativtexte, Tastaturbedienung) und im Footer auf die Barrierefreiheitserklärung der Schule verlinken oder eine eigene kurze Erklärung anbieten (offener Punkt).
- **Name und Logo:** Kein Name, Logo oder Namensbestandteil bekannter Marken, auch nicht abgewandelt. [Q4, S. 2 f.] Vor der Veröffentlichung "PRINT&BITE" auf Kollisionen prüfen (Markenregister). Logo und Gestaltung stammen von Schülerinnen und Schülern: Nutzungsrechte für die Schule schriftlich festhalten (offener Punkt).
- **Produkte:** Patentierte oder lizenzierte Produkte nicht nachbauen. [Q4, S. 3 f.] Bei 3D-Modellen aus Online-Sammlungen die Lizenz prüfen; Lizenzen mit "nicht kommerziell" (z. B. Creative Commons "NC") erlauben keinen Verkauf.
- **Werbeaussagen:** "Was draufsteht, muss auch drin sein"; Angaben wie "Bio" oder "Öko" nur mit Nachweis, nichts als "reduziert" bewerben, was zum Normalpreis verkauft wird (UWG). [Q4, S. 4]
- **Snacks:** Kennzeichnung und Allergene gelten beim Verkauf am Stand (Aushang, Kopie); Hinweise der Handreichung S. 22 f. Wenn die Website Snacks mit Zutaten beschreibt, müssen diese Angaben stimmen. [Q4]
- **Kooperation BBS II (Holz):** Auf der Website erkennbar machen, welche Produkte in Kooperation entstehen; Fotos von BBS-II-Schülerinnen und -Schülern brauchen Einwilligungen über die BBS II (offener Punkt).
- **Fertige Vorlagen** (Impressum-Generatoren, Shop-Baukästen) enthalten oft Bausteine für Unternehmen (OS-Link, Handelsregister, USt-ID, § 19 UStG). Nicht ungeprüft übernehmen.

---

## 9. Checkliste Pflichtinhalte (für die Spezifikation)

Pflicht:

- [ ] Footer auf jeder Seite: Status-Hinweis "Schülerfirma der BBS I Lüneburg - pädagogisches Schulprojekt" + Links "Impressum" und "Datenschutz"
- [ ] Impressum nach 2.2/2.3: Land Niedersachsen, vertreten durch Schulleitung (voller Name), Anschrift BBS I, E-Mail, Telefon, Firmenbezeichnung PRINT&BITE, Hinweis pädagogisches Projekt
- [ ] Datenschutzerklärung nach 4.2 (auf Basis RLSB-Muster, angepasst)
- [ ] Kontakt der oder des schulischen Datenschutzbeauftragten (DSE, zusätzlich im Impressum)
- [ ] HTTPS auf der ganzen Website
- [ ] Schriften, Skripte, Bilder, Videos selbst gehostet; keine Drittanbieter beim Seitenaufruf
- [ ] Personenfotos nur mit schriftlicher, website-spezifischer Einwilligung; Widerruf führt zur Entfernung
- [ ] Kontakt: `mailto:` auf funktionale Schuladresse + Telefon (Formular nur mit TLS, DSE-Abschnitt, ggf. AV-Vertrag)

Nur unter Bedingung:

- [ ] Verantwortlicher nach § 18 Abs. 2 MStV (betreuende Lehrkraft), wenn es einen News-/Blog-Bereich gibt
- [ ] Zwei-Klick-Lösung oder Consent, wenn doch eine Karte oder YouTube eingebettet wird
- [ ] Hinweis Verbraucherschlichtung (§ 36 VSBG), falls nach Klärung erforderlich
- [ ] USt-IdNr., falls das Land für Schulen eine solche führt und Angabe gefordert ist

Nicht aufnehmen:

- [ ] keine Steuerhinweise (insbesondere kein "§ 19 UStG")
- [ ] keine echte Rechtsform ("GmbH"), kein Handelsregister
- [ ] kein Link zur EU-OS-Plattform
- [ ] keine Social-Media-Plugins, keine Analyse-Tools, kein Google reCAPTCHA, keine Google Fonts vom Google-Server

---

## 10. Offene Punkte für Schulleitung, Schulträger und RLSB

| Nr. | Frage | Wer kann antworten |
| --- | --- | --- |
| 1 | Ist PRINT&BITE als Schulprojekt genehmigt, hat der Landkreis zugestimmt, und gibt es eine Kooperationsvereinbarung, die die Website als Vertriebs-/Werbeweg nennt? | Schulleitung, Landkreis Lüneburg |
| 2 | Wo wird die Website gehostet (Subdomain der Schul-Website, Server des Schulträgers, Dienstleister der Schul-Website, anderer Anbieter)? Wer schließt den Auftragsverarbeitungsvertrag? | Schulleitung, IT des Landkreises |
| 3 | Domain: Subdomain von bbs1-lueneburg.de (MK-Empfehlung) oder eigene Domain? Wer wäre Domaininhaber? | Schulleitung, Schul-IT |
| 4 | Funktionale E-Mail-Adresse für PRINT&BITE in der Schul-Domain anlegen; wer liest das Postfach (auch in den Ferien)? | Schulleitung, Schul-IT |
| 5 | Name der Schulleitung fürs Impressum bestätigen; Kontaktadresse der oder des Datenschutzbeauftragten der BBS I | Schulleitung |
| 6 | Gibt es einen News-/Blog-Bereich? Dann: Ist die betreuende Lehrkraft einverstanden, als Verantwortliche(r) nach § 18 Abs. 2 MStV genannt zu werden? | Schulleitung, betreuende Lehrkraft |
| 7 | Fallen die Umsätze von PRINT&BITE (3D-Druck, Holzprodukte, Snacks) unter § 4 Nr. 21 UStG laut BMF-Schreiben vom 24.10.2025? Muss eine USt-IdNr. ins Impressum? | Schulleitung über Fachbereich Umsatzbesteuerung (1 U) der RLSB Osnabrück |
| 8 | Findet die Arbeit in der Schülerfirma im Pflichtunterricht statt? Wenn ja: Unter welchen Bedingungen dürfen Fotos von Schülerinnen und Schülern überhaupt auf die Website (LfD: bei Pflichtveranstaltungen i. d. R. keine freiwillige Einwilligung)? Welches Einwilligungsformular wird genutzt? | Schulleitung, Datenschutzbeauftragte(r) |
| 9 | Rechtsgrundlage und Speicherdauer der Server-Logfiles (Art. 6 Abs. 1 lit. e i. V. m. § 3 NDSG statt lit. f wie im RLSB-Muster?) | Datenschutzbeauftragte(r), Datenschutzdezernat der RLSB |
| 10 | Ist das Land/die Schule beim Verkauf durch die Schülerfirma "Unternehmer" im Sinne des § 36 VSBG, sodass ein Hinweis zur Verbraucherschlichtung nötig ist? | Schulleitung, ggf. RLSB/MK |
| 11 | Wer hält die Rechte an Name und Logo "PRINT&BITE" (von Schülerinnen und Schülern gestaltet)? Nutzungsrechte schriftlich an die Schule einräumen? Markenrecherche? | Schulleitung |
| 12 | Kooperation mit BBS II: Wer ist Verkäufer der Holzprodukte, wie wird die BBS II auf der Website genannt, wer holt Einwilligungen für Fotos von BBS-II-Schülerinnen und -Schülern ein? | Schulleitungen BBS I und BBS II |
| 13 | Eigene Barrierefreiheitserklärung oder Verweis auf die Erklärung der Schul-Website? | Schulleitung |
| 14 | Abschließende Kontrolle des Online-Auftritts durch Regionalkoordination Nachhaltige Schülerfirmen (RLSB Lüneburg), schulische Datenschutzperson und Schulleitung, wie in der Handreichung empfohlen [Q4, S. 21][Q31] | Schulleitung |

---

## Quellen

Alle abgerufen am 01.10.2026.

- [Q1] Digitale-Dienste-Gesetz (DDG), § 5 Allgemeine Informationspflichten: https://www.gesetze-im-internet.de/ddg/__5.html ; § 7 Beschränkte Verantwortlichkeit: https://www.gesetze-im-internet.de/ddg/__7.html
- [Q2] Medienstaatsvertrag (MStV) in der Fassung des Siebten Medienänderungsstaatsvertrags, in Kraft seit 01.12.2025, nichtamtliche Fassung der Medienanstalten, §§ 18, 24: https://www.die-medienanstalten.de/fileadmin/user_upload/Rechtsgrundlagen/Gesetze_Staatsvertraege/Medienstaatsvertrag_MStV.pdf
- [Q3] NiBiS Datenschutzportal (NLQ), "Impressumpflicht für Schulhomepages" (Stand 2026-03-03): https://datenschutz.nibis.de/2013/09/19/impressumpflicht-fuer-schulhomepages/
- [Q4] Niedersächsisches Kultusministerium, "Handreichung für Schülerfirmen in Niedersachsen zur Gründung, Organisation und Durchführung" (Januar 2023), Seitenangaben nach der Paginierung im Dokument: https://www.mk.niedersachsen.de/download/193308/Handreichung_Schuelerfirmen_organisiert_wie_richtige_Unternehmen_.pdf
- [Q5] § 43 NSchG (VORIS): https://voris.wolterskluwer-online.de/browse/document/75629065-64fb-388f-a31e-16f9a05b78fb
- [Q6] § 102 NSchG Schulträger (VORIS): https://voris.wolterskluwer-online.de/browse/document/753243cf-c08a-3a24-b77b-17669c1066f5
- [Q7] Bildungsportal Niedersachsen (RLSB), "Häufige Fragen und Antworten zum Datenschutz" (Stand 01.03.2023): https://bildungsportal-niedersachsen.de/schulorganisation/datenschutz-an-schulen/dsgvo-an-schulen-und-studienseminaren/haeufige-fragen-und-antworten-zum-datenschutz ; Muster AV-Vertrag: https://bildungsportal-niedersachsen.de/schulorganisation/datenschutz-an-schulen/dsgvo-an-schulen-und-studienseminaren/datenverarbeitung-im-auftrag
- [Q8] RLSB, "Muster Datenschutzerklärung Schulhomepage" (Stand 01.12.2020, DOCX), verlinkt auf: https://bildungsportal-niedersachsen.de/schulorganisation/datenschutz-an-schulen/dsgvo-an-schulen-und-studienseminaren/informationspflichten-gemaess-art-13-dsgvo
- [Q9] Bildungsportal Niedersachsen, "Umsatzsteuer an Schulen und Studienseminaren" (Stand 2026): https://bildungsportal-niedersachsen.de/schulorganisation/schule-leiten/umsatzsteuer-an-schulen-und-studienseminaren
- [Q10] BMF-Schreiben vom 24.10.2025, III C 3 - S 7179/00054/001/094, "Umsatzsteuerbefreiung für unmittelbar dem Schul- und Bildungszweck dienende Leistungen", UStAE 4.21.1 Abs. 15 bis 17 und Anwendungsregelungen: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-24-ust-befreiung-schul-und-bildungszweck.html
- [Q11] § 4 Nr. 21 UStG: https://www.gesetze-im-internet.de/ustg_1980/__4.html
- [Q12] Verordnung (EU) 2016/679 (DSGVO), insbesondere Art. 6, 7, 12, 13, 37, 77: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679
- [Q13] § 3 NDSG (VORIS): https://voris.wolterskluwer-online.de/browse/document/ab12945d-0f99-3e51-87b8-4ad140fbb958
- [Q14] LfD Niedersachsen, "Anfertigung und Veröffentlichung von Personenfotografien im öffentlichen Bereich" (Themenseite Schulen): https://www.lfd.niedersachsen.de/schulen/schulen_veroffentlichung_von_personenfotografien_durch_offentliche_stellen/
- [Q15] NiBiS Datenschutzportal, "»Ja, ich will« - die datenschutzrechtliche Einwilligung im schulischen Kontext" (20.02.2024): https://datenschutz.nibis.de/2024/02/20/ja-ich-will-diedatenschutzrechtliche-einwilligung-imschulischen-kontext/
- [Q16] Kunsturhebergesetz (KUG) §§ 22, 23: https://www.gesetze-im-internet.de/kunsturhg/__22.html , https://www.gesetze-im-internet.de/kunsturhg/__23.html
- [Q17] TDDDG § 25 Schutz der Privatsphäre bei Endeinrichtungen: https://www.gesetze-im-internet.de/ttdsg/__25.html ; § 19 Technische und organisatorische Vorkehrungen: https://www.gesetze-im-internet.de/ttdsg/__19.html
- [Q18] Datenschutzkonferenz, "Orientierungshilfe der Aufsichtsbehörden für Anbieter:innen von digitalen Diensten (OH Digitale Dienste)", Version 1.2, November 2024, Randnummern 76, 101, 106: https://www.datenschutzkonferenz-online.de/media/oh/OH_Digitale_Dienste.pdf
- [Q19] LfD Niedersachsen, "Informationen für Betreiber von Webseiten und Apps (digitale Dienste)" (Stand Juli 2025): https://www.lfd.niedersachsen.de/dsgvo/informationen_fur_betreiber_von_webseiten/informationen-fur-betreiber-von-webseiten-und-apps-digitale-dienste-164589.html
- [Q20] LfD Niedersachsen, Pressemitteilung "Abmahnungen zu Datenschutzverstößen auf Webseiten vermeiden - Google Fonts lokal einbinden" (mit Verweis auf LG München I, 20.01.2022, 3 O 17493/20): https://lfd.niedersachsen.de/startseite/infothek/presseinformationen/abmahnungen-zu-datenschutzverstossen-auf-webseiten-vermeiden-google-fonts-lokal-einbinden-217509.html
- [Q21] NiBiS Datenschutzportal, "Erreichbarkeit des/der Datenschutzbeauftragten" (19.01.2021): https://datenschutz.nibis.de/2021/01/19/erreichbarkeit-des-der-datenschutzbeauftragten/
- [Q22] EuGH, Urteil vom 16.10.2008, C-298/07 (deutsche internet versicherung): https://curia.europa.eu/juris/liste.jsf?language=de&num=C-298/07
- [Q23] BGH, Urteil vom 20.07.2006, I ZR 228/03 (Anbieterkennzeichnung im Internet), Fundstellen: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2006-07-20&Aktenzeichen=I+ZR+228%2F03
- [Q24] § 36 VSBG: https://www.gesetze-im-internet.de/vsbg/__36.html
- [Q25] Verordnung (EU) 2024/3228 (Aufhebung der Verordnung (EU) Nr. 524/2013 über Online-Streitbeilegung): https://eur-lex.europa.eu/legal-content/DE/ALL/?uri=CELEX%3A32024R3228
- [Q26] Niedersächsisches Behindertengleichstellungsgesetz (NBGG), § 9 Abs. 2 und 3, §§ 9a bis 9e (Textfassung schure.de): https://www.schure.de/84200/nbgg.htm
- [Q27] OpenStreetMap, Copyright und Lizenz (ODbL, Quellenangabe): https://www.openstreetmap.org/copyright ; Tile Usage Policy: https://operations.osmfoundation.org/policies/tiles/
- [Q28] NiBiS Datenschutzportal, "Links zu anderen Web-Inhalten": https://datenschutz.nibis.de/2013/09/16/links-zu-anderen-web-inhalten/ ; "Haftung für den Internetauftritt" (OLG Celle 13 U 95/15): https://datenschutz.nibis.de/2016/04/13/haftung-fuer-den-internetauftritt/
- [Q29] NiBiS Datenschutzportal, "Checkliste Schulhomepage" (Stand 2022-01-17): https://datenschutz.nibis.de/2015/11/25/checkliste-fuer-die-schulhomepage/ ; "Fashion-ID-Urteil: Gemeinsame Verantwortlichkeit für Social Plugins": https://datenschutz.nibis.de/2020/09/08/fashion-id-urteil-gemeinsame-verantwortlichkeit-fuer-social-plugins/
- [Q30] Website der BBS I Lüneburg (Ist-Stand, zum Abgleich): Impressum https://www.bbs1-lueneburg.de/impressum , Datenschutz https://www.bbs1-lueneburg.de/datenschutz.html , Barrierefreiheit https://www.bbs1-lueneburg.de/barrierfreiheit.html
- [Q31] Bildungsportal Niedersachsen, Beratung Schülerfirmen (Regionalkoordination): https://bildungsportal-niedersachsen.de/beratung-unterstuetzung/onlineportal-bu/uebergreifend/schuelerfirmen
- [Q32] Research zu #6, Schriftlizenzen (Branch `research/schriftlizenzen`): https://github.com/HAITI-03-Messeretter/print-and-bite/blob/research/schriftlizenzen/docs/research/schriftlizenzen.md

> **Nochmals: Keine Rechtsberatung.** Rechtslage und Verwaltungsvorgaben können sich ändern (zuletzt z. B. Umsatzsteuer 2025/2026). Vor der Veröffentlichung der Website Impressum und Datenschutzerklärung von Schulleitung und Datenschutzbeauftragter/m freigeben lassen.
