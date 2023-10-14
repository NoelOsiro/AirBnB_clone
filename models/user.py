#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of User.

        Args:
            *args: Variable length positional arguments (not used).
            **kwargs: Variable length keyword arguments. If provided,
            the instance attributes will be set based on these keyword
            arguments.
        """
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """
        Return a dictionary with all instances of a class.
        """
        from models import storage
        return storage.all(cls)
