from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title: str = Field(min_lenght=1, max_lenght=100)
    content: str = Field(min_lenght=1)
    author: str = Field(min_lenght=1, max_lenght=50)


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
