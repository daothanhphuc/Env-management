from sqlalchemy.orm.session import Session
from db.schemas import UserBase, GroupBase
from db.models import dbHuyen, dbXa

# Create new huyen
def huyen(db: Session, request: UserBase):
    huyen = dbHuyen(
        huyen_name = request.huyen_name,
        description = request.description
    )
    db.add(huyen)
    db.commit()
    db.refresh(huyen)
    return huyen
def xa (db: Session, request: UserBase):
    new_xa = dbXa(
        xa_name = request.xa_name,
        description = request.description
    )
    db.add(new_xa)
    db.commit()
    db.refresh(new_xa)
    return new_xa
def list_huyen(db: Session):
    return db.query(dbHuyen).all()
def list_xa(db: Session):
    return db.query(dbXa).all()
