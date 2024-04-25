from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import repository
from data import get_db_session
from web.schemas import User, UserCreate, Like

app = FastAPI()


async def get_db():
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = repository.get_user_by_chat_id(db, chat_id=user.chat_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repository.create_user(db=db, user=user)


@app.put("/users/", response_model=User)
def update_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = repository.update_user(db, user_update=user)
    if db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    return db_user


@app.get("/users/", response_model=User)
def get_user(chat_id: str, db: Session = Depends(get_db)):
    db_user = repository.get_user_by_chat_id(db, chat_id=chat_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    else:
        return db_user


@app.get("/get_match_users/", response_model=List[Like])
def get_pairing_suggestion_users(chat_id: str, db: Session = Depends(get_db)):
    users = repository.get_match_users(db, chat_id)
    if not users:
        raise HTTPException(status_code=400, detail="No matching users found")
    return users


@app.put("/execute_like/", response_model=Like)
def like_suggestion(like_id: int, is_executed: bool, db: Session = Depends(get_db)):
    like = repository.update_like(db, like_id, is_executed)
    if not like:
        raise HTTPException(status_code=400, detail="like not found")
    return like


@app.get("/get_liked_users/", response_model=List[User])
def get_liked_users(chat_id: str, db: Session = Depends(get_db)):
    liked_users = repository.get_liked_users(chat_id, db)
    if not liked_users:
        raise HTTPException(status_code=400, detail="user not found")
    else:
        return liked_users


@app.get("/get_liker_users/", response_model=List[User])
def get_liker_users(chat_id: str, db: Session = Depends(get_db)):
    liker_users = repository.get_liker_users(chat_id, db)
    if not liker_users:
        raise HTTPException(status_code=400, detail="user not found")
    else:
        return liker_users
