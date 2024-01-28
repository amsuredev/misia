import psycopg2
from psycopg2._psycopg import connection


class DatabaseConnection:
    def __init__(self, host, database, user, password):
        self.__host = host
        self.__database = database
        self.__user = user
        self.__password = password
        self.__connection = None

    def connect(self) -> connection:
        conn = psycopg2.connect(host=self.__host,
                                database=self.__database,
                                user=self.__user,
                                password=self.__password)
        conn.autocommit = True
        self.__connection = conn
        return self.__connection



