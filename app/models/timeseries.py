from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class TimeSeries(Base):
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(Integer)
    location = relationship("Location")
    location_id = Column(Integer, ForeignKey("location.id"))
