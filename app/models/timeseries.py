from sqlalchemy import Column, ForeignKey, Integer, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class TimeSeries(Base):
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(Integer)
    min_temp = Column(Float)
    max_temp = Column(Float)
    mean_temp = Column(Float)
    location = relationship("Location")
    location_id = Column(Integer, ForeignKey("location.id"))
    __table_args__ = (UniqueConstraint('location_id', 'timestamp', name='location_timestamp'),)

    def __init__(self, timestamp, location_id, min_temp, max_temp, mean_temp):
        self.timestamp = timestamp
        self.location_id = location_id
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.mean_temp = mean_temp
