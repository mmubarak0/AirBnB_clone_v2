#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """A-base class for all hbnb models."""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model."""
        __now = datetime.now()
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = __now
            self.updated_at = __now
        else:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = datetime.strptime(
                        kwargs.get("created_at", __now.isoformat()),
                        "%Y-%m-%dT%H:%M:%S.%f"
                )
            self.updated_at = datetime.strptime(
                        kwargs.get("updated_at", __now.isoformat()),
                        "%Y-%m-%dT%H:%M:%S.%f"
                )

    def __str__(self):
        """Return a string representation of the instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current time when instance is changed."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format."""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete this instance."""
        from models import storage
        storage.delete(self)
