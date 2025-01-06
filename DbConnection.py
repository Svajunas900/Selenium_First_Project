import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

class PostgresDbConnection:
    _instance = None

    def cursor(cls, *args, **kwargs):
        cls._instance = cls._instance.cursor(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=POSTGRES_HOST, port=POSTGRES_PORT)
        return cls._instance

