
from typing import Optional
from pydantic import BaseModel, EmailStr


class signupReq(BaseModel):
  email: EmailStr
  password: str

class signupRes(BaseModel):
  email: EmailStr


class UserLogin(BaseModel):
  email: EmailStr
  password: str


class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  email: Optional[str] = None