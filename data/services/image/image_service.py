from data.repositories.image.image_repository import ImageRepository


class ImageService:

    def __init__(self, image_repository: ImageRepository):
        self.__image_repository = image_repository

