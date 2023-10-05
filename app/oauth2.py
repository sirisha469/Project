from jose import JWTError, jwt
from app.config import settings
from datetime import datetime, timedelta

from app.database import get_db
from . import schemas
from fastapi import Depends,status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
  to_encode = data.copy()

  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

  return encoded_jwt


def verify_access_token(token: str, credential_exception):

  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

    id: str = payload.get("user_id")

    if id is None:
      raise credential_exception
    
    token_data = schemas.TokenData(id=id)

  except JWTError:
    raise credential_exception
  
  return token_data


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
  credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

  return verify_access_token(token, credential_exception)

  