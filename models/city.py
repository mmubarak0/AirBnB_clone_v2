#!/usr/bin/python3
"""City Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os

storage_engine = os.environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """The city class, contains state ID and name."""

    if (storage_engine == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""
