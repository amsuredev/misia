from psycopg2._psycopg import connection


class ImageRepository:
    def __init__(self, conn: connection):
        self.__connection = conn

    def create(self, data: tuple):
        with self.__connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO images (photo)
            VALUES (%s)
            """, data)

    def add_image_to_user(self, data: tuple):
        with self.__connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO user_images(user_id, image_id)
            VALUES (%s, %s)
            """, data)

    def get_user_images(self, user_id):
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
            select photo
            from user_images
            JOIN users ON user_images.user_id = users.id
            JOIN images ON user_images.image_id = images.id
            WHERE user_id = '{user_id}'
            """)