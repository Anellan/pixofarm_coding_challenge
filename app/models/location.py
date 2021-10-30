from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Location(Base):
    id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, nullable=True)
    latitude = Column(Float)
    longitude = Column(Float)
    altitude = Column(Float)
    continent = relationship("Continent")
    continent_id = Column(Integer, ForeignKey("continent.id"))
