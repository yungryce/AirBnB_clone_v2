#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Deserialize JSON file to objects"""
        self.reload()

    # def get(self, cls, id):
    #     """Retrieve an object"""
    #     if cls is not None and type(cls) is str and id is not None and\
    #        type(id) is str and cls in classes:
    #         key = cls + '.' + id
    #         obj = self.__objects.get(key, None)
    #         return obj
    #     else:
    #         return None

    # def count(self, cls=None):
    #     """Count number of objects in storage"""
    #     total = 0
    #     if type(cls) == str and cls in classes:
    #         total = len(self.all(cls))
    #     elif cls is None:
    #         total = len(self.__objects)
    #     return total
