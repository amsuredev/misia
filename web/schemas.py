from pydantic import BaseModel


class ImageBase(BaseModel):
    photo: str
    user_id: str


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True


class LikeBase(BaseModel):
    superior_id: str
    interior_id: str
    is_executed: bool
    is_mutual: bool


class LikeCreate(BaseModel):
    pass


class Like(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    chat_id: str
    first_name: str
    age: int
    sex: str
    sex_preference: str
    profile_message: str
    town: str
    country: str
    is_active: bool
    images: list[Image] = []
    likes_as_superior: list[Like]
    likes_as_interior: list[Like]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
