
from pydantic import BaseModel, EmailStr


class signupReq(BaseModel):
  email: EmailStr
  password: str

class signupRes(BaseModel):
  email: EmailStr