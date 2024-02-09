class MatchmakerRepository:
    def __init__(self, conn, limit_suggestion_num=10):
        self.__connection = conn

    def like_suggestion(self, superior_id, interior_id) -> None:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE pairing_suggestions
                           SET was_decision = true, was_liked = true
                           WHERE superior_id = '{superior_id}' and interior_id = '{interior_id}'
                           """)

    def dislike_suggestion(self, superior_id, interior_id) -> None:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           UPDATE pairing_suggestions
                           SET was_decision = true, was_liked = false
                           WHERE superior_id = '{superior_id}' and interior_id = '{interior_id}'
                           """)

    async def get_pairing_suggestion(self, superior_id):
        suggestion = await self.__next_suggestion(superior_id)
        if suggestion:
            return suggestion
        else:
            self.__create_suggestions(superior_id=superior_id)
            return await self.__next_suggestion(superior_id=superior_id)

    def __create_suggestions(self, superior_id) -> None:
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

    async def __next_suggestion(self, superior_id) -> tuple:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           select * from pairing_suggestions
                           where superior_id = {superior_id} and was_decision = false
                           limit 1
                           """)
            return cursor.fetchone()
