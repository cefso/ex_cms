from pydantic import BaseModel, Field


class QuerySchema(BaseModel):
    page: int = Field(default=1, title="current page number")
    size: int = Field(default=10, title="size of page", ge=10, le=100)


class PageSchema(BaseModel):
    page: int
    page_size: int
    total: int

    class Config:
        orm_mode = False
