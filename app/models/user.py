from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.session import Session
from db import db

class User(db.Model):
  __tablename__ = 'users'
  
  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  email: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
  password: Mapped[str] = mapped_column(db.String, nullable=True)

  session: Mapped['Session'] = relationship('Session', back_populates='user', uselist=False, cascade='all, delete')
