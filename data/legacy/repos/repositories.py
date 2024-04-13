from sqlalchemy.orm import Session# Make sure to adjust the import path

from data.sql_alchemy.models import Image, User, Like


class ImageRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_image(self, image):
        self.session.add(image)
        self.session.commit()

    def get_image_by_id(self, image_id):
        return self.session.query(Image).filter(Image.id == image_id).first()

    # Add more methods as needed for your specific use cases


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id).first()

    # Add more methods as needed for your specific use cases


class LikeRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_like(self, like):
        self.session.add(like)
        self.session.commit()

    def get_like_by_id(self, like_id):
        return self.session.query(Like).filter(Like.id == like_id).first()

    # Add more methods as needed for your specific use cases