from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
import src.admins.schemas as _schemas
import src.admins.models as _models
from src.lib.hash import Hash

def create_admin(db: Session, request: _schemas.AdminCreate):
    admin = db.query(_models.Admin).filter(_models.Admin.username == request.username).first()
    if(admin is not None):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username taken!")
    
    new_admin = _models.Admin(
        username = request.username,
        email = request.email,
        login = request.login,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

def get_admins(db: Session):
    return db.query(_models.Admin).all()

def get_admin_by_id(id: int, db: Session):
    return db.query(_models.Admin).filter(_models.Admin.id == id).first()


def get_admins_by_username(adminname: str, db: Session):
    return db.query(_models.Admin).filter(_models.Admin.username == adminname).all()


def update_admin(id: int, db: Session, request: _schemas.AdminCreate):
    admin = db.query(_models.Admin).filter(_models.Admin.id == id)
    admin.update(_models.Admin(
        username = request.username,
        email = request.email,
        login = request.login,
        password = Hash.bcrypt(request.password)
    ))
    db.commit()
    return admin.all()

def delete_admin(id: int, db: Session):
    admin = db.query(_models.Admin).filter(_models.Admin.id == id).first()
    if(admin is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    db.delete(admin)
    db.commit()
    return admin