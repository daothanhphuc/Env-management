from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from db.database import engine
from db import models, admin_permission, guest_permission
from router import register_user, delete_user, statistic_user, search_accounts, add, create_group


class MyItem(BaseModel):
    imgbase64: str

app = FastAPI()

# Mount static files (CSS, JS, images) từ thư mục 'fe'
app.mount("/static", StaticFiles(directory="fe"), name="static") #"/static" là đường dẫn trang web cho các file CSS

# Chỉ định thư mục 'fe' chứa các file HTML
templates = Jinja2Templates(directory="fe")
#Router cho các trang web
@app.get("/", response_class=HTMLResponse) #"/" là đường dẫn trang web
async def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})




app.include_router(register_user.router)
app.include_router(delete_user.router)
app.include_router(statistic_user.router)
app.include_router(search_accounts.router)
app.include_router(add.router)
app.include_router(create_group.router)





models.Base.metadata.create_all(engine)


