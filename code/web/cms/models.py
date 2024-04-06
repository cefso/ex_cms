from pydantic import BaseModel


class AliyunAuthSchema(BaseModel):
    access_key_id: str
    access_key_secret: str
    endpoint: str = 'metrics.cn-hangzhou.aliyuncs.com'

    class Config:
        orm_mode = True
