from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    # return 'heyy'
    # return {"message": "Hello, World!"}
    return {'data': {'name': 'John'}}


@app.get('/about')
def abou():
    return {'data': 'This is the about page'}