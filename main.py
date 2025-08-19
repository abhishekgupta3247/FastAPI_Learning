from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    # return 'heyy'
    # return {"message": "Hello, World!"}
    return {'data': 'blog list'}


@app.get('/blog/1')
def show():
    return {'data': 1}