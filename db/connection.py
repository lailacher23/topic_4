import psycopg2
from sqlalchemy import create_engine

from config import DATABASE_URL


def create_connection():
    return psycopg2.connect(DATABASE_URL)


def get_engine():
    return create_engine(DATABASE_URL)
