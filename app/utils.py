
from jose import JWTError
from passlib.context import CryptContext
from fastapi import HTTPException,status

from app.oauth2 import ALGORITHM, SECRET_KEY


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
  return pwd_context.hash(password)

def verify(plain_password, hashed_pwd):
  return pwd_context.verify(plain_password, hashed_pwd)


def verify_access_token(token: str, credential_exception):

  try:
    payload = JWTError.decode(token, SECRET_KEY, algorithms=ALGORITHM)

    user: str = payload.get("user_id")

  except:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid token",
      headers={"WWW.Authenticate": "Bearer"}
    )
  return user