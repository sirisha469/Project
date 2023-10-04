from fastapi import FastAPI
from app import models
from .router import signup
from app.database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(signup.router)

@app.get("/")
def root():
  return {"message": "Hello world"}