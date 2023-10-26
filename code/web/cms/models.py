from pydantic import BaseModel


class AliyunAuthSchema(BaseModel):
    access_key_id: str
    access_key_secret: str
    endpoint: str = None

    class Config:
        orm_mode = True
