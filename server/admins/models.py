import datetime as _dt
import sqlalchemy as _sql
from database import Base

class Admin(Base):
    __tablename__="admins"
    id = _sql.Column(_sql.Integer, index=True, primary_key=True)
    username = _sql.Column(_sql.String, unique=True)
    email = _sql.Column(_sql.String)
    login = _sql.Column(_sql.String)
    password = _sql.Column(_sql.String)

class Token(Base):
    __tablename__="tokens"
    id = _sql.Column(_sql.Integer, index=True, primary_key=True)
    admin_id = _sql.Column(_sql.Integer, _sql.ForeignKey(Admin.id))
    token = _sql.Column(_sql.String, unique=True)
    time = _sql.Column(_sql.Integer, default=3600)
    last_updated = _sql.Column(_sql.DateTime)