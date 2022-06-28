import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True) # autoincrement = True
    name = Column(String)
    number = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # auto



