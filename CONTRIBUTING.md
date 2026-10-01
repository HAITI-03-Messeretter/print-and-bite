# Contributing

Dieses Repository wird gemeinsam im Rahmen des Berufsschulprojekts **Print & Bite** entwickelt.

## Workflow

Änderungen werden grundsätzlich über einen eigenen Branch und einen Pull Request eingebracht.

Direkte Änderungen auf `main` sollen vermieden werden.

## Branch-Namen

Folgende Präfixe werden verwendet:

- `feat/` – neue Funktionen
- `fix/` – Fehlerbehebungen
- `docs/` – Dokumentation
- `refactor/` – Überarbeitung bestehenden Codes
- `chore/` – Wartung, Konfiguration oder organisatorische Änderungen

Wenn ein Issue vorhanden ist, soll dessen Nummer im Branch-Namen enthalten sein.

Beispiele:

```text
feat/12-shopping-cart
fix/18-price-calculation
docs/21-readme
refactor/24-order-service
chore/5-github-setup
```

Branch-Namen werden kleingeschrieben und Wörter mit Bindestrichen getrennt.

Branches sollen grundsätzlich vom aktuellen Stand von `main` erstellt werden.

## Pull Requests

Vor dem Erstellen eines Pull Requests:

- Änderungen lokal prüfen
- unnötige Debug-Ausgaben entfernen
- relevante Änderungen dokumentieren
- wenn möglich das zugehörige Issue verknüpfen

Beispiel:

```text
Closes #12
```

Pull Requests sollen eine verständliche Beschreibung der vorgenommenen Änderungen enthalten.

## Reviews

Jeder Pull Request muss vor dem Merge von mindestens einem anderen Entwickler geprüft werden.

Dabei gelten folgende Regeln:

- Der Autor eines Pull Requests darf die eigene Änderung nicht selbst freigeben.
- Offene Review-Kommentare und Änderungswünsche müssen vor dem Merge geklärt werden.
- Änderungen, die nach einem Review vorgenommen werden, sollen erneut geprüft werden, wenn sie den bereits geprüften Code wesentlich verändern.
- Erst nach erfolgreichem Review darf der Pull Request in `main` übernommen werden.

## Commits

Commit-Nachrichten sollen kurz und verständlich beschreiben, was geändert wurde.

Folgende Präfixe werden empfohlen:

- `feat:` – neue Funktion
- `fix:` – Fehlerbehebung
- `docs:` – Dokumentation
- `refactor:` – Überarbeitung bestehenden Codes
- `chore:` – Wartung oder Konfiguration

Beispiele:

```text
feat: add shopping cart
fix: correct price calculation
docs: update project documentation
refactor: simplify order service
chore: update repository configuration
```

## Merge

Pull Requests werden per **Squash Merge** in `main` übernommen.

Nach erfolgreichem Merge wird der zugehörige Branch gelöscht.
