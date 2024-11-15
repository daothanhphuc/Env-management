from fastapi import APIRouter, Depends
from db.schemas import UserBase, UserDisplay, DeleteDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import admin_permission
router = APIRouter(
    prefix="/search_accounts",
    tags=["search_accounts"]
)
@router.post("/search_guest_accounts", response_model=UserDisplay)
def search_guest_accounts(find_id: int, db: Session=Depends(get_db)):
    return admin_permission.search_guest_accounts(db=db, find_id=find_id)