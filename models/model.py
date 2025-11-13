from sqlalchemy import String, Column, Integer, Float, DateTime
from database import Base
from datetime import datetime, timezone
from pydantic import BaseModel




class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )


class PersonCreate(BaseModel):
    emotion : str
    confidence : float


class PersonResponse(PersonCreate):
    id : int
    created_at : datetime


