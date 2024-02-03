class SympathiesRepository:
    def __init__(self, conn):
        self.__connection = conn

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

    def get_pairing_suggestion(self, superior_id):#mvp
        # check if exists suggestion for superior_id with was_decision = false - on this stage can be omited
        # create not existing superior suggestion
        # return created superior suggestion
        # create suggestion
        # return created suggestion
        #
        pass

    def create_all_possible_suggestions(self, superior_id):
        # take profiles from your town
        # no personal suggestion and no mutual (obratnyj like)
        # create vsem takim suggestionam jebanuc nachuj
        pass

    def get_pairing_suggestions(self, superior_id, preferable_suggestions_num):
        pass
        # check if exist suggestions for this user with was_decision = false
        # if yes return max (preferable_suggestions_num, available_suggestion_number)
        # if no create preferable_suggestions_num suggestions
        # return max (preferable_suggestions_num, available_suggestion_number)

    def get_matches(self,  superior_id):
        #return list of searchable liked_id from likes
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           Select liked_id, liker_id from likes
                           where liker_id = 5 or liked_id = 5 and was_decision = true and mutual = true                           
                           SELECT 
                               CASE 
                                   WHEN liker_id = 5 THEN liked_id 
                                   WHEN liked_id = 5 THEN liker_id 
                               END as user_id
                           FROM likes
                           WHERE (liker_id = 5 OR liked_id = 5) AND was_decision = true AND mutual = true;
                           """)
        # здесь не хватает лайкер_айди или лайкд_айди на селекте

    def get_liked_profiles(self, superior_id):#те кого я лайкнул, которые не мэтч, те не мутуал лайки из likes
        with self.__connection.cursor() as cursor:
            cursor.execute(f"""
                           select liked_id 
                           from likes 
                           where liker_id = {superior_id} and (was_decision = false or mutual = false)
                           """)
        pass

#предложка, те кого я лайкнул, мэтчи