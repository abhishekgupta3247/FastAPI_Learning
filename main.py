from typing import Optional
from fastapi import FastAPI

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
    return limit
    return {'data': {'1', '2'}}