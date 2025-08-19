from fastapi import FastAPI

app = FastAPI()

# @app.get("/blog?limit=10&published=true")
@app.get("/blog")
def index(limit, published):
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
def show(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}