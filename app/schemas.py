from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):  # inheriting PostBase attributes
    id: int
    email: EmailStr
    created_at: datetime  # define response to receive which data to get

    class Config:
        orm_mode = True  # converts SQLAlchemy model to pydantic model


class Post(PostBase):  # inheriting PostBase attributes
    id: int
    created_at: datetime  # define response to receive which data to get
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True  # converts SQLAlchemy model to pydantic model


class PostOut(PostBase):  # inheriting PostBase attributes
    Post: Post
    votes: int

    class Config:
        orm_mode = True  # converts SQLAlchemy model to pydantic model


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
