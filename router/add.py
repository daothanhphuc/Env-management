from fastapi import APIRouter, Depends
from db.schemas import UserBase, RoleDisplay, LFBase, LFDisplay, constructionBase, constructionDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import guest_permission, admin_permission
from db import livestock, construction
router = APIRouter(
    prefix="/add",
    tags=["add"]
)
@router.post("/add_guest_role", response_model=RoleDisplay)
def add_guest_role(db: Session=Depends(get_db)):
    return guest_permission.create_guest_role(db)
@router.post("/add_admin_role", response_model=RoleDisplay)
def add_admin_role(db: Session=Depends(get_db)):
    return admin_permission.create_admin_role(db)
#Livestock
@router.post("/add_LF", response_model=LFDisplay)
def add_LF(request: LFBase, db: Session=Depends(get_db)):
    return livestock.add_LF(db, request)
@router.post("/add_staff_for_LF", response_model= LFDisplay)
def add_staff(request: LFBase, farm_id: int, db: Session=Depends(get_db)):
    return livestock.add_staff(db, request, farm_id)
@router.post("/add_condition_for_LF", response_model= LFDisplay)
def add_condition(request: LFBase, farm_id: int, conditions: str, db: Session=Depends(get_db)):
    return livestock.add_condition(db, request, farm_id, conditions)
#Construction    
@router.post("/add_waterFocus", response_model= constructionDisplay)
def add_construction(request: constructionBase, db: Session=Depends(get_db)):
    return construction.new_water_focus(db, request)
@router.post("/add_waterRetail", response_model= constructionDisplay)
def add_construction(request: constructionBase, db: Session=Depends(get_db)):
    return construction.new_water_retail(db, request)
# Legal document
