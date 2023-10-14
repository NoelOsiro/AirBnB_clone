#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """
    @classmethod
    def all(cls):
        """
        Return a dictionary with all instances of a class.
        """
        return storage.all(cls)
    place_id = ""
    user_id = ""
    text = ""
