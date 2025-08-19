from fastapi import FastAPI

app = FastAPI()

@app.post('/blog')
def create():
    return 'creating'
    # return {"message": "Blog created successfully"}