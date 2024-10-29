from fastapi import APIRouter, Depends
from db.schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import crud


router = APIRouter(
    prefix="/register_user",
    tags=["register_user"]
)

@router.post("/new_user", response_model=UserDisplay)
def create_user(request: UserBase, db: Session=Depends(get_db), group_id: int = None, role_name: str = "guest"):
    return crud.create_user(db, request, group_id, role_name)
@router.post("/new_admin", response_model=UserDisplay)
def create_admin(request: UserBase, db: Session=Depends(get_db), role_name: str = "admin"):
    return crud.create_admin(db, request, role_name)

