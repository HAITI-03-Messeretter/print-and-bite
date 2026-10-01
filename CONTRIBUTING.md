# Contributing

Dieses Repository wird gemeinsam im Rahmen des Berufsschulprojekts **Print & Bite** entwickelt.

## Workflow

Jede Änderung kommt über einen eigenen Branch und einen Pull Request in `main`.

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

Pull Requests werden mit der Vorlage `.github/PULL_REQUEST_TEMPLATE.md` erstellt. Ihre Checkliste ist vor dem Erstellen vollständig abgehakt.

Ein zugehöriges Issue wird im Pull Request verknüpft:

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

## Beispiel: vom Issue zum Merge

Für ein Issue #12 "Warenkorb":

```bash
git switch main
git pull
git switch -c feat/12-shopping-cart
# ... Änderungen ...
git add .
git commit -m "feat: add shopping cart"
git push -u origin feat/12-shopping-cart
gh pr create --fill
```

Im Pull Request steht `Closes #12`. Nach dem Review wird per Squash Merge übernommen und der Branch danach gelöscht.
