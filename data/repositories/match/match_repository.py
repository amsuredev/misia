class MatchRepository:
    def like_potential_match(self, superior_id, interior_id) -> None:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE likes
                           SET was_decision = true, mutual = true
                           WHERE liker_id = '{superior_id}' and liked_id = '{interior_id}'
                           """)

    def dislike_potential_match(self, superior_id, interior_id) -> None:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE likes
                           SET was_decision = true, mutual = false
                           WHERE liker_id = '{superior_id}' and liked_id = '{interior_id}'
                           """)

    def get_matches(self,  superior_id) -> tuple:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           Select liked_id, liker_id from likes
                           where liker_id = {superior_id} or liked_id = {superior_id} and was_decision = true and mutual = true                           
                           SELECT 
                               CASE 
                                   WHEN liker_id = {superior_id} THEN liked_id 
                                   WHEN liked_id = {superior_id} THEN liker_id 
                               END as user_id
                           FROM likes
                           WHERE (liker_id = {superior_id} OR liked_id = {superior_id}) AND was_decision = true AND mutual = true;
                           """)
            return cursor.fetchall()

    def get_liked_profiles(self, superior_id) -> tuple:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           select liked_id 
                           from likes 
                           where liker_id = {superior_id} and (was_decision = false or mutual = false)
                           """)
            return cursor.fetchall()
