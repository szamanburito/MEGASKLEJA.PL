import sqlalchemy.orm as _orm

from typing import TYPE_CHECKING, List

from fastapi import FastAPI, Depends
from gallery.schemas import CreateImage
from gallery.services import get_db

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/api/images")
async def get_images():
    return []

@app.post("/api/image")
async def create_image(image: CreateImage, db: _orm.Session = Depends(get_db)):
    return []