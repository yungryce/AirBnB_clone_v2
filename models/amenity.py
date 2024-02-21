#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.type_storage == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
