from psycopg2._psycopg import connection

class UserRepository:
    def __init__(self, conn: connection):
        self.__connection = conn

    async def create(self, data: tuple):
        with self.__connection.cursor() as curs:
            curs.execute("""
            INSERT INTO users (chat_id, first_name, age, sex, sex_preference, profile_message, town, country, active)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, data
            )
            return None

    async def get(self, chat_id):
        with self.__connection.cursor() as curs:
            curs.execute(f"""
            select * from users
            where chat_id = '{chat_id}'
            """)
        return curs.fetchone()

    async def update(self, column_name, data: tuple, chat_id):
        with self.__connection.cursor() as curs:
            curs.execute(f"""
            UPDATE users
            SET {column_name} = (%s) 
            WHERE chat_id = '{chat_id}'
            """, data)

        return None

    async def delete(self, chat_id):
        with self.__connection.cursor() as curs:
            curs.execute(f"""
            DELETE FROM users 
            WHERE chat_id = '{chat_id}'
            """)