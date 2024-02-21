#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

if models.type_storage == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if models.type_storage == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize a class
        Args:
            *args: variable number of positional args in a tuple
            **kwargs (dict): Key/value pairs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key not in ["__class__"]:
                    setattr(self, key, value)

    def __str__(self):
        """should print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__:s}] ({self.id:s}) {self.__dict__}"

    def save(self):
        """updates public instance updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary representation of the BaseModel instance
          using a shallow copy method"""
        obj_dict = self.__dict__.copy()
        for key, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in obj_dict:
            del obj_dict["_sa_instance_state"]
        return obj_dict

    def delete(self):
        """Delete current instance from storage by calling its delete method"""
        models.storage.delete(self)
