from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.qr_code import QRCode
from sqlalchemy import DateTime
from datetime import datetime
from db import db

class Scan(db.Model):
  __tablename__ = 'scans'
  
  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

  qr_code: Mapped['QRCode'] = relationship('QRCode', back_populates='scan')