#!/usr/bin/python3
"""Database storage engine using SQLAlchemy with a mysql+mysqldb database
connection.
"""

from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER,
                                                 HBNB_MYSQL_PWD,
                                                 HBNB_MYSQL_HOST,
                                                 HBNB_MYSQL_DB),
            pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls and cls in classes:
            for obj in self.__session.query(cls):
                new_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for clss in classes.values():
                for obj in self.__session.query(clss):
                    new_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
