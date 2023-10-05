from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from app.database import get_db
from sqlalchemy.orm import Session
from app import schemas, models,utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(
  tags=['Authentication']
)

@router.post("/login")
# def login(user_credentials : schemas.UserLogin, db: Session = Depends(get_db)):
def login(user_credentials : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

  # {
      # "username": email
      # "password": password
  # }
  user = db.query(models.Signup).filter(models.Signup.id == user_credentials.username).first()

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  
  if utils.verify(user_credentials.password, user.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  
  access_token = oauth2.create_access_token(data = {"user_id": user.id})

  return {"access_token": access_token, "token_type":"Bearer"} 