# Recepty DB

Aplikace pro správu receptů.

## Požadavky

*   Python 3.6+
*   pip

## Instalace

1.  Vytvořte virtuální prostředí:

    ```bash
    python3 -m venv venv
    ```
2.  Aktivujte virtuální prostředí:

    *   Na Linuxu/macOS:

        ```bash
        source venv/bin/activate
        ```
    *   Na Windows:

        ```bash
        venv\\Scripts\\activate
        ```
3.  Nainstalujte závislosti:

    ```bash
    pip install -r requirements.txt
    ```

## Konfigurace

Vytvořte soubor `.env` v kořenovém adresáři s následujícími proměnnými:

*   `DATABASE_URL`: URL databáze (např. `mysql://user:password@host/database`)
*   `FLASK_SECRET_KEY`: Tajný klíč pro Flask aplikaci
*   `PORT`: Port, na kterém má aplikace běžet (výchozí: 4000)

Příklad:

```
DATABASE_URL=mysql://user:password@host/database
FLASK_SECRET_KEY=random_secret_key
PORT=4000
```

## Spuštění

1.  Ujistěte se, že máte nastavenou databázi a nakonfigurovanou v souboru `.env`.
2.  Spusťte aplikaci:

```bash
python run.py
```

## Počáteční data

Můžete použít skript `init.sql` pro vložení počátečních dat do databáze.

## Popis

Aplikace umožňuje ukládání, úpravu a prohlížení receptů.