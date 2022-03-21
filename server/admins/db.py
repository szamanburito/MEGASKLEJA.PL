from sqlalchemy.orm.session import Session
import admins.schemas as _schemas
import admins.models as _models
from lib.hash import Hash

def create_admin(db: Session, request: _schemas.AdminCreate):
    new_admin = _models.Admin(
        **request.dict(),
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
        **request.dict(),
        password = Hash.bcrypt(request.password)
    ))
    db.commit()
    return admin.all()

def delete_admin(id: int, db: Session):
    admin = db.query(_models.Admin).filter(_models.Admin.id == id).first()
    db.delete(admin)
    db.commit()
    return admin