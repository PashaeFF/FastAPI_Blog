from typing import List, Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str



class User(BaseModel):
    name: str
    email: str
    password: str

class UserBlogs(BaseModel):
    title: str

    class Config():
        orm_mode = True



class ShowUser(BaseModel):
    id: int
    name: str
    blogs: List[UserBlogs]
    class Config():
        orm_mode = True

class ShowCreator(BaseModel):
    name: str
    class Config():
        orm_mode = True
    
class ShowBlog(BaseModel):
    title: str
    body: str
    creator:  ShowCreator

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None