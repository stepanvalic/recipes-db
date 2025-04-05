import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()

def test_db_connection():
    try:
        engine = sqlalchemy.create_engine(os.getenv('DATABASE_URL'))
        connection = engine.connect()
        connection.close()
        assert True
    except Exception as e:
        print(e)
        assert False
