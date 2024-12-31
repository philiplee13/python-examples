import psycopg


class DatabaseConnection:
    __connection = None

    def __new__(cls):
        if cls.__connection is None:
            uri: str = "postgresql://postgres:postgres@localhost:5431"
            cls.__connection = psycopg.connect(uri)
        else:
            print("Connection was already created...")
        return cls
