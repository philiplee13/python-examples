"""
config class that instantiates db connection
"""

import psycopg2
from psycopg2.extras import RealDictCursor


class Config:
    def __init__(self):
        self.conn: psycopg2.extensions.connection = self.connect()

    def connect(self) -> psycopg2.extensions.connection:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            port=5432,
            host="localhost",
            cursor_factory=RealDictCursor,
        )
        return conn
