from sqlalchemy import Column, String
from .database import Base

class Signup(Base):
  __tablename__ = "signup"

  email = Column(String, nullable=False, primary_key = True)
  password = Column(String, nullable=False)
