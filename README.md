# Recipes DB

A recipe management application.

## Requirements

*   Python 3.6+
*   pip

## Installation

1.  Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```
2.  Activate the virtual environment:

    *   On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```
    *   On Windows:

        ```bash
        venv\\Scripts\\activate
        ```
3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Create a `.env` file in the root directory with the following variables:

*   `DATABASE_URL`: URL of the database (e.g., `mysql://user:password@host/database`)
*   `FLASK_SECRET_KEY`: Secret key for Flask application
*   `PORT`: Port for the application to run on (default: 4000)

Example:

```
DATABASE_URL=mysql://user:password@host/database
FLASK_SECRET_KEY=random_secret_key
PORT=4000
```

## Usage

1.  Make sure you have a database set up and configured in the `.env` file.
2.  Run the application:

```bash
python run.py
```

## Initial data

You can use the `init.sql` script to insert initial data into the database.

## Description

The application allows you to store, edit, and view recipes.