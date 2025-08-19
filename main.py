from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    # return 'heyy'
    # return {"message": "Hello, World!"}
    return {'data': 'blog list'}


@app.get('/blog/{id}')
def show(id):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def show(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}