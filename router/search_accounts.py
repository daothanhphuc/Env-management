from fastapi import APIRouter, Depends
from db.schemas import UserBase, UserDisplay, DeleteDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import admin_permission
router = APIRouter(
    prefix="/search",
    tags=["search"]
)
@router.post("/all/", response_model=list[UserDisplay])
# def search_guest_accounts(find_id: int, db: Session=Depends(get_db)):
#     return admin_permission.search_guest_accounts(db=db, find_id=find_id)
async def get_all_users(db: Session=Depends(get_db)):
    # Fetch the list of dbUser objects from the database
    users = admin_permission.get_all(db=db, request=UserBase)
    return [UserDisplay.from_orm(user) for user in users]