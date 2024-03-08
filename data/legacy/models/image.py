class Image:
    def __init__(self, id: str, user_id: str, photo: str):
        self.__id = id
        self.__user_id = user_id
        self.__photo = photo

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def photo(self):
        return self.__photo





