from typing import List

from pydantic import BaseModel, Field

from web import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(255), unique=True)
    userName = db.Column(db.String(255))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
            del dict["id"]
            return dict


class UserSchema(BaseModel):
    userId: str
    userName: str

    class Config:
        orm_mode = True


class UsersSchema(BaseModel):
    page: int
    page_size: int
    total: int
    users: List[UserSchema]

    class Config:
        orm_mode = False


class QuerySchema(BaseModel):
    page: int = Field(default=1, title="current page number")
    size: int = Field(default=10, title="size of page", ge=10, le=100)
