from sqlalchemy import Column, Integer, String, Float
from app.db.base_class import Base


class Location(Base):
    id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, nullable=True, unique=True)
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, location_name, latitude, longitude):
        self.location_name = location_name
        self.latitude = latitude
        self.longitude = longitude
