from sqlalchemy import TIMESTAMP, Column, String, Integer, text, Boolean
from .database import Base

class Signup(Base):
  __tablename__ = "signup"

  id = Column(Integer,nullable=False, primary_key=True)
  email = Column(String, nullable=False)
  password = Column(String, nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
  is_verify = Column(Boolean, nullable=False, default=False)


