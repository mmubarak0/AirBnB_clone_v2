#!/usr/bin/python3
"""City Module for HBNB project."""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os

storage_engine = os.environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """The city class, contains state ID and name."""

    __tablename__ = "cities"
    if (storage_engine == "db"):
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        #places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""
