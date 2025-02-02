from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime


class Blog (Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(String(500))
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)