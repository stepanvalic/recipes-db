# Plán práce na více souborovou aplikaci s webovým rozhraním

Tento dokument popisuje plán práce na aplikaci databáze receptů. Aplikace umožní vytváření, editaci a zobrazování receptů s možností nahrávání PDF souborů. Níže je rozpis kroků a úkolů.

---

## 1. Návrh projektu a technologický stack

- **Programovací jazyk:** Python
- **Webový framework:** Flask (alternativně Django, pokud bude vyžadována robustnější struktura)
- **Databáze:** MySQL
- **ORM:** SQLAlchemy (volitelně, pro jednodušší práci s databází)
- **Správa konfigurací:** .env (např. pomocí python-dotenv)
- **Frontend:** HTML, CSS, JavaScript (možná knihovna pro rychlejší vývoj formulářů)
- **Úložiště souborů:** Místní složka na serveru pro PDF soubory

---

## 2. Návrh databáze

- **Tabulka `recipes`:**
  - `id`: primární klíč, autoinkrement
  - `name`: jméno receptu (string)
  - `url`: URL originálního receptu (string)
  - `description`: popisek receptu (text)
  - `pdf_path`: cesta k nahranému PDF souboru (string)
  - Volitelné: datum vytvoření/aktualizace (timestamp)

---

## 3. Klíčové funkce aplikace

### a) Vytváření nových receptů
- **Formulář:**
  - Pole pro jméno receptu
  - Pole pro URL originálního receptu
  - Textové pole pro popisek receptu
  - Možnost nahrání PDF souboru
  - Tlačítko pro uložení
- **Backend:**
  - Validace vstupních dat a PDF souboru
  - Uložení PDF souboru do serverové složky
  - Uložení dat do MySQL databáze

### b) Hlavní stránka (dashboard)
- **Funkce:**
  - Výpis všech receptů (zobrazení pouze názvů)
  - Vyhledávač pro snadné nalezení receptu podle jména
  - Odkazy na detailní zobrazení receptu nebo editaci

### c) Detail receptu
- **Funkce:**
  - Zobrazení všech detailů receptu
  - Možnost zobrazení PDF přímo v prohlížeči (např. v `<embed>` nebo `<iframe>`)

### d) Editace receptu
- **Funkce:**
  - Umožnit změnu jména, popisku a URL
  - Možnost nahrát nový PDF soubor nebo odebrat stávající

---

## 4. Bezpečnost a konfigurace

- **Citlivé údaje:**
  - Uložení databázových přihlašovacích údajů, tajných klíčů apod. do souboru `.env`
- **Ochrana nahrávaných souborů:**
  - Validace typu souboru (povolit pouze PDF)
  - Ošetření názvů souborů, aby nedošlo ke kolizím či bezpečnostním rizikům

---

## 5. Vývojové prostředí a struktura projektu

### a) Struktura projektu
- `/app`
  - `__init__.py` – inicializace aplikace a konfigurace
  - `routes.py` – definice endpointů (vytváření, editace, zobrazení receptů)
  - `models.py` – definice databázových modelů (např. pomocí SQLAlchemy)
  - `forms.py` – definice formulářů pro zadávání dat (volitelné, např. pomocí Flask-WTF)
  - `/templates` – HTML šablony (hlavní stránka, formulář, detail receptu, editace)
  - `/static` – statické soubory (CSS, JS, obrázky)
- `/uploads` – složka pro nahrané PDF soubory
- `.env` – soubor s konfigurací a citlivými údaji
- `requirements.txt` – seznam Python knihoven

### b) Počáteční kroky
1. Vytvořit virtuální prostředí a nainstalovat požadované balíčky:
   - Flask, mysqlclient/pymysql, python-dotenv, SQLAlchemy (volitelně Flask-WTF)
2. Inicializovat repozitář (Git) a přidat `.gitignore` (včetně `.env` a `/uploads`).

---

## 6. Postup implementace

1. **Inicializace projektu:**
   - Vytvořit základní strukturu složek a inicializovat Flask aplikaci.
2. **Konfigurace a připojení k databázi:**
   - Nastavit `.env` soubor s přihlašovacími údaji a načíst je v aplikaci.
   - Vytvořit databázovou schému a definovat model `Recipe`.
3. **Implementace funkcionality pro vytváření receptů:**
   - Vytvořit HTML formulář pro zadávání receptu.
   - Ošetřit upload PDF souboru a uložit soubor do `/uploads`.
   - Uložit data do databáze.
4. **Hlavní stránka a vyhledávač:**
   - Načíst a zobrazit seznam receptů z databáze.
   - Implementovat vyhledávací funkci podle jména receptu.
5. **Detail a editace receptu:**
   - Vytvořit stránku pro zobrazení detailů receptu a vložení PDF (pomocí `<embed>`/`<iframe>`).
   - Implementovat formulář a logiku pro editaci receptu a aktualizaci dat v databázi.
6. **Testování a ladění:**
   - Testovat jednotlivé funkce, validovat vstupy a zabezpečit aplikaci.
7. **Dokumentace a nasazení:**
   - Vytvořit dokumentaci k nasazení a případně připravit Docker kontejner či další řešení pro produkční prostředí.

---

## 7. Automatizované zálohování pomocí Gitu

Aby bylo možné sledovat historii změn a automaticky si zálohovat práci, bude nastaven jednoduchý systém verzování pomocí Gitu.

### a) Git repozitář
- Inicializovat Git repozitář ve složce projektu
- Přidat `.gitignore` (např. pro `__pycache__`, `.env`, `/uploads`, virtuální prostředí apod.)

### b) Automatizovaný Git skript

Vytvořit jednoduchý bash nebo Python skript např. `git_backup.sh`, který bude:
1. Přidávat všechny nové/změněné soubory do Gitu (`git add .`)
2. Vytvářet commit s automatickým popiskem obsahujícím datum, čas a volitelně i výpis posledních změn
3. (Volitelně) push na vzdálený repozitář (např. GitHub, GitLab)

```bash
#!/bin/bash
# git_backup.sh
MESSAGE="Auto backup - $(date '+%Y-%m-%d %H:%M:%S')"
git add .
git commit -m "$MESSAGE"
# git push origin main  # odkomentovat, pokud je nastavený vzdálený repozitář
```
---