#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This module defines the BaseModel class,
    which serves as the base class for all
    models in the application.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
            *args: Variable length positional arguments (not used).
            **kwargs: Variable length keyword arguments.
                If provided, the instance attributes will
                be set based on these keyword arguments.

        Attributes:
            id (str): Unique identifier for the instance.
            created_at : Date and time the instance was created.
            updated_at : Date and time the instance was last updated.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(
                        self,
                        key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    @classmethod
    def all(cls):
        """
        Return a dictionary with all instances of a class.
        """
        return storage.all(cls)

    def save(self):
        """
        Update the 'updated_at' attribute with
        the current datetime and save the instance to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        Return a dictionary representation
        of the instance.

        Returns:
            dict: A dictionary containing all
            instance attributes and their values.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self) -> str:
        """
        Return a string representation of the instance.

        Returns:
            str: A string in the format
            '[<class name>] (<self.id>) <self.__dict__>'.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns:
            str: A string in the format
            '[<class name>] (<self.id>) <self.__dict__>'.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)
