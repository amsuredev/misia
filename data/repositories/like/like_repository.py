from psycopg2._psycopg import connection


class LikeRepository:

    def __init__(self, conn: connection):
        self.__connection = conn

    async def create(self, data: tuple):
        with self.__connection.cursor() as curs:
            curs.execute("""
            INSERT INTO likes (superior_id, interior_id, is_executed, mutual)
            values (%s, %s, %s, %s)
            """, data)

    async def get(self, chat_id):
        with self.__connection.cursor() as curs:
            curs.execute("""
            SELECT * FROM likes
            WHERE 
            """)

    async def update(self, column_name, data: tuple, like_id):
        pass

    async def delete(self, like_id):
        pass