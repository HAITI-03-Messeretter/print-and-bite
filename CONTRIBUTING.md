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
chore/5-github-setup
```

Branch-Namen werden kleingeschrieben und Wörter mit Bindestrichen getrennt.

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

Pull Requests werden von mindestens einem anderen Entwickler geprüft, bevor sie in `main` übernommen werden.

## Commits

Commit-Nachrichten sollen kurz und verständlich beschreiben, was geändert wurde.

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
EOF

git add CONTRIBUTING.md
git commit -m "docs: add contributing guidelines"
git push -u origin docs/contributing
