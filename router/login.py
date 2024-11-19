from fastapi import APIRouter, HTTPException, Depends
from db.schemas import LoginRequest
from sqlalchemy.orm import Session
from db.database import get_db
from db.hash import Hash
from db import models

router = APIRouter(
    prefix="/login",
    tags=["login"]
)

@router.post("/verify/")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Tìm người dùng dựa trên tên đăng nhập
    user = db.query(models.dbUser).filter(models.dbUser.username == data.username).first()

    # Kiểm tra nếu người dùng không tồn tại
    if not user or user.role_id != data.role_id:
        raise HTTPException(status_code=404, detail="User not found")

    # Kiểm tra mật khẩu
    if not Hash.verify(data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {"message": "Login successful"}

