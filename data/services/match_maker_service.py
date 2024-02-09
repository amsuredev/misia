from data.repositories.sympathies_repository import SympathiesRepository


class MatchMakerService:
    def __init__(self, sympathies_repository: SympathiesRepository):
        self.__sympathies_repository = sympathies_repository

    def get_potential_pair(self, superior_id):
        pass

    def like_potential_pairing(self):
        pass