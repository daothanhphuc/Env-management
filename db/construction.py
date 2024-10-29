from sqlalchemy.orm.session import Session
from db.schemas import UserBase, GroupBase
from db.models import dbHuyen, dbXa, dbWaterFocus, dbWaterRetail, dbWaterReport, dbWaterStatistic

def new_water_focus(db: Session, request: UserBase):
    new_focus = dbWaterFocus(
        focus_name = request.focus_name,
        description = request.description
    )
    db.add(new_focus)
    db.commit()
    db.refresh(new_focus)
    return new_focus
def new_water_retail(db: Session, request: UserBase):
    new_retail = dbWaterRetail(
        retail_name = request.retail_name,
        description = request.description
    )
    db.add(new_retail)
    db.commit()
    db.refresh(new_retail)
    return new_retail

# List construction base on xa_id
def find_focus_construction (db: Session, xa_id: int):
    return db.query(dbWaterFocus).filter(dbWaterFocus.xa_id == xa_id).all()
def find_retail_construction (db: Session, xa_id: int):
    return db.query(dbWaterRetail).filter(dbWaterRetail.xa_id == xa_id).all()

