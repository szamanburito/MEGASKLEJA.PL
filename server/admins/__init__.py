from typing import TYPE_CHECKING, List

from fastapi import APIRouter, Depends, status
from database import get_db
import admins.db as admin_db

from sqlalchemy.orm.session import Session
import admins.schemas as _schemas

router = APIRouter(
    prefix="",
    tags=["admin"]
)

# Create admin
@router.post("/admin", response_model=_schemas.AdminResponse, status_code=status.HTTP_201_CREATED)
async def create_admin(request: _schemas.AdminCreate, db: Session = Depends(get_db)) -> _schemas.AdminResponse:
    return admin_db.create_admin(db, request)

# Read admins
@router.get("/admins", response_model=List[_schemas.AdminResponse], status_code=status.HTTP_200_OK)
async def get_all_admins(db: Session = Depends(get_db)):
    return admin_db.get_admins(db)

@router.get("/admin/{id}", response_model=_schemas.AdminResponse, status_code=status.HTTP_200_OK)
async def get_admins_by_id(id: int, db: Session = Depends(get_db)):
    return admin_db.get_admin_by_id(id, db)

@router.get("/admins/{username}", response_model=List[_schemas.AdminResponse], status_code=status.HTTP_200_OK)
async def get_admins_by_username(username: str, db: Session = Depends(get_db)):
    return admin_db.get_admins_by_username(username, db)

# Update admin
@router.post("/admin/{id}/update", response_model=_schemas.AdminResponse, status_code=status.HTTP_201_CREATED)
def update_admin(id: int, request: _schemas.AdminCreate, db: Session = Depends(get_db)):
    return admin_db.update_admin(id, db, request)

# Delete admin
@router.delete("/admin/{id}/delete", response_model=_schemas.AdminResponse, status_code=status.HTTP_200_OK)
def delete_admin(id: int, db: Session = Depends(get_db)):
    return admin_db.delete_admin(id, db)