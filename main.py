from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


# @app.get("/blog?limit=10&published=true")
# def inde():
#     return {'data': 'blog list'}


# @app.get("/")
# def index():
#     return {'data': 'blog list'}

# @app.get("/blog")
# def index(limit = 10, published: bool = True, sort: Optional[str] = None):
#     if published:
#         return {'data': f'{limit} published blogs from the db'}
#     else:
#         return {'data': f'{limit} blogs from the db'}

# class Blog(BaseModel): 
#     title: str
#     body: str
#     published: Optional[bool]

# @app.post("/blog")
# def create_blog(request: Blog):

#     return {'data': f"Blog is created with '{request.title}'"}

# @app.get("/blog/unpublished")
# def unpublished():
#     return {'data': 'all unpublished blogs'}


# @app.get("/blog/{id}")
# def show(id: int):
#     #fetch blog with id = id
#     return {'data': id}


# @app.get("/blog/{id}/comments")
# def comments(id):
#     #fetch blog with id = id
#     return {'data': {1,2}}


if __name__ == "__main__":
    uvicorn.run(app, host ="127.0.0.1", port = 8000)