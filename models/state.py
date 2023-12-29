#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.city import City

storage_engine = os.environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class."""

    __tablename__ = "states"
    if (storage_engine == 'db'):
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state"
        )
    else:
        name = ""

        @property
        def cities(self):
            """Return a list of cities instances."""
            import models
            return [
                i for i in models.storage.all(City).values()
                if i.state_id == self.id
            ]
