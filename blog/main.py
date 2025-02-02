from typing import Optional
from fastapi import FastAPI, Depends
from . import schemas, models, database
from sqlalchemy.orm import Session
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def hello_world():
    return {"hello": "world"}



def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog")
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@app.get('/blogs')
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)