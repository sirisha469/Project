from fastapi import FastAPI
from app import models
from .router import signup, authentication
from app.database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(signup.router)
app.include_router(authentication.router)

@app.get("/")
def root():
  return {"message": "Hello world"}