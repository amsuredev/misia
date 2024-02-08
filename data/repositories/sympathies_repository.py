import asyncio


class SympathiesRepository:

    def __init__(self, conn):
        self.__connection = conn
        self.__num_profile_suggestions_create = 10

    def like_suggestion(self, superior_id, interior_id):
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE pairing_suggestions
                           SET was_decision = true, was_liked = true
                           WHERE superior_id = '{superior_id}' and interior_id = '{interior_id}'
                           """)

    def like_potential_match(self, superior_id, interior_id):
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE likes
                           SET was_decision = true, mutual = true
                           WHERE liker_id = '{superior_id}' and liked_id = '{interior_id}'
                           """)

    def dislike_suggestion(self, superior_id, interior_id):
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE pairing_suggestions
                           SET was_decision = true, was_liked = false
                           WHERE superior_id = '{superior_id}' and interior_id = '{interior_id}'
                           """)

    def dislike_potential_match(self, superior_id, interior_id):
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE likes
                           SET was_decision = true, mutual = false
                           WHERE liker_id = '{superior_id}' and liked_id = '{interior_id}'
                           """)

    async def get_pairing_suggestions(self, superior_id):
        suggestion = await self.next_suggestion(superior_id)
        if suggestion:
            return suggestion
        else:
            self.create_suggestion(superior_id=superior_id)
            return await self.next_suggestion(superior_id=superior_id)

    def create_suggestion(self, superior_id):
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           INSERT INTO public.pairing_suggestions (superior_id, interior_id)
                           SELECT {superior_id} as superior_id, id as interior_id
                           FROM public.users u
                           WHERE u.town = (SELECT town FROM public.users WHERE id = {superior_id})
                           AND u.sex = (SELECT sex_preference FROM public.users WHERE id = {superior_id})
                           AND u.sex_preference = (SELECT sex FROM public.users WHERE id = {superior_id})
                           AND u.active = TRUE
                           AND NOT EXISTS (
                               SELECT 1
                               FROM public.pairing_suggestions ps
                               WHERE ps.superior_id = {superior_id}
                               AND ps.interior_id = u.id
                           )
                           LIMIT {self.__num_profile_suggestions_create}
                           """)

    async def next_suggestion(self, superior_id):
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           select * from pairing_suggestions
                           where superior_id = {superior_id} and was_decision = false
                           limit 1
                           """)
            return cursor.fetchone()

    def get_matches(self,  superior_id):
        #return list of searchable liked_id from likes
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

    def get_liked_profiles(self, superior_id):#те кого я лайкнул, которые не мэтч, те не мутуал лайки из likes
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           select liked_id 
                           from likes 
                           where liker_id = {superior_id} and (was_decision = false or mutual = false)
                           """)
