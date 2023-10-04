from fastapi import Depends
from fastapi import APIRouter
from app.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
  prefix="/login",
  tags=['Authentication']
)

@router.post("/")
def login(db: Session = Depends(get_db)):
  return 67