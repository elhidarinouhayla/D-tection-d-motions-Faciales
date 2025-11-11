from sqlalchemy import String, Column, Integer, Float, DateTime
from database import Base
from datetime import datetime
from pydantic import BaseModel




class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class PersonCreate(BaseModel):
    emotion : str
    confidence : float


class PersonRespense(PersonCreate):
    id : int
    created_at : datetime


