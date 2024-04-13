from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from data import get_db_session
from web.schemas import User, UserCreate
import repositories

app = FastAPI()


async def get_db():
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = repositories.get_user_by_chat_id(db, chat_id=user.chat_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repositories.create_user(db=db, user=user)


@app.put("/users/", response_model=User)
def update_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = repositories.update_user(db, user_update=user)
    if db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    return db_user


@app.get("/users/", response_model=User)
def get_user(chat_id: str, db: Session = Depends(get_db)):
    db_user = repositories.get_user_by_chat_id(db, chat_id=chat_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    else:
        return db_user


@app.get("/get_pairing_suggestion_users/", response_model=List[User])
def get_pairing_suggestion_users(chat_id: str, count: int = 100, db: Session = Depends(get_db)):
    users = repositories.get_pairing_suggestion_users(db, chat_id, count)
    if not users:
        raise HTTPException(status_code=400, detail="No pairing suggestions can be generated")
    return users


# @app.get("/users/{item_id}/", response_model=list[User])
# def get_matches():
#     return "s"
