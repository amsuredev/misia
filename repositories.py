from typing import List, Optional

from sqlalchemy.orm import Session
from data.sql_alchemy import models
from data.sql_alchemy.models import User, Like
from web import schemas
from random import choice


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_chat_id(db: Session, chat_id: str):
    return db.query(models.User).filter(models.User.chat_id == chat_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_update: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.chat_id == user_update.chat_id).first()
    if db_user:
        for key, value in user_update.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def filter_users_with_like(session: Session, current_user: User, potential_users: List[User]) -> List[User]:
    liked_user_ids = [like.interior_id for like in current_user.likes_as_superior]
    filtered_users = [user for user in potential_users if user.id not in liked_user_ids]

    # Additional check for existing likes with reversed roles and not executed
    existing_reversed_likes = session.query(Like).filter(
        Like.superior_id.in_([user.id for user in filtered_users]),
        Like.interior_id == current_user.id,
        Like.is_executed is True  # Assuming False means not executed
    ).all()

    # Remove potential users who have existing likes with reversed roles and not executed
    filtered_users = [user for user in filtered_users if
                      not any(like.superior_id == user.id for like in existing_reversed_likes)]

    return filtered_users


def get_potential_users(session: Session, current_user: User) -> List[User]:
    potential_users = (session.query(User).filter(
        User.sex == current_user.sex_preference,
        User.sex_preference == current_user.sex,
        User.town == current_user.town,
        User.id != current_user.id  # Exclude the current user
    ).all())
    return potential_users


def create_like(session: Session, current_user: User, potential_users: List[User]) -> Optional[Like]:
    filtered_users = filter_users_with_like(session, current_user, potential_users)
    if filtered_users:
        liked_user = choice(filtered_users)
        like = Like(superior=current_user, interior=liked_user, is_executed=False)
        session.add(like)
        session.commit()
        return like
    else:
        return None


def get_pairing_suggestion_users(db, chat_id, count):
    # создать каунт раз паиринг суггестион для данного юзера
    # вернуть каунт до включит. кол-во паириннг суггестион для данного юзера (возможно меньше)
    # лучше вернуть не нан
    db.query(models.User).filter(models.User.chat_id != chat_id)
    return None
