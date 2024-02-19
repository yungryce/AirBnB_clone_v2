#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class for all hbnb models"""
            
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
        # my_dict['updated_at'] = self.updated_at.isoformat()
        # my_dict['created_at'] = self.created_at.isoformat()
        return obj_dict