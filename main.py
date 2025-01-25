from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def hello_world():
    return {"hello": "world"}




class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(request: Blog):

    return {"data": request}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)