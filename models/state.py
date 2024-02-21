#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.type_storage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        # super(BaseModel, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)

    if models.type_storage != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            from models.city import City
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
