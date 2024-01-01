#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Amenity class."""

    __tablename__ = "amenity"
    if (storage_engine == "db"):
        name = Column(String(128), nullable=False)
    else:
        name = ""
