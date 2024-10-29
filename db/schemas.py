from pydantic import BaseModel
from typing import Optional, List
# from sqlalchemy.sql.sqltypes import Integer, Date,TIMESTAMP, Boolean
from datetime import datetime

class UserBase(BaseModel):
    fullname: str
    username: str
    email: str
    password: str
    # status: Optional[str] = "active"

class UserDisplay(BaseModel):
    fullname: str
    username: str
    email: str
    role_id: int
    class Config():
        from_attributes = True
class DeleteDisplay(BaseModel):
    username: str
    class Config():
        from_attributes = True 
        # from_attributes = True la de chuyen tu camelCase sang snake_case
class UserUpdate(BaseModel):
    fullname: Optional[str]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]

class GroupBase(BaseModel):
    group_name: str
    description: str
class GroupDisplay(BaseModel):
    group_name: str
    description: str
    class Config():
        from_attributes = True

class RoleDisplay(BaseModel):
    name: str
    description: str
    class Config():
        from_attributes = True

# Livestock facility base
class LFBase(BaseModel):
    name: str
    owner: str
    register_date: str
class LFDisplay(BaseModel):
    name: str
    owner: str
    register_date: str
    class Config():
        from_attributes = True 

# Construction base
class constructionBase(BaseModel):
    name: str
    location: str
    status: str
    construction_year: str
class constructionDisplay(BaseModel):
    name: str
    location: str
    status: str
    construction_year: str
    class Config():
        from_attributes = True
