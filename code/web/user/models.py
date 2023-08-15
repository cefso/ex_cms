from typing import List

from pydantic import BaseModel

from code.web import db
from code.web.common.schema import PageSchema


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


class UsersSchema(PageSchema):
    users: List[UserSchema]

    class Config:
        orm_mode = False

