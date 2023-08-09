from pydantic import BaseModel

from web import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(255), unique=True)
    userName = db.Column(db.String(255))


class UserSchema(BaseModel):
    userId: str
    userName: str

    class Config:
        orm_mode = True
