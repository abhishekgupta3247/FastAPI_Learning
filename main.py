from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# @app.get("/blog?limit=10&published=true")
# @app.get("/blog?sort=latest")
@app.get("/blog")
def index(limit = 10, published : bool = True, sort: Optional[str] = None):
    # return published
    # only get 10 published blogs
    if published:
        # fetch only published blogs
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def show():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id : int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
# id is a path parameter. limit is a query parameter.
def show(id, limit=10):
    # fetch comments of blog with id = id
    # return limit
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
# def create_blog(blog: Blog):
def create_blog(request: Blog):
    return {'data': f'blog is created with title as {request.title}'}