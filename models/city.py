#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """
    state_id = ""
    name = ""

    @classmethod
    def all(cls):
        """
        Return a dictionary with all instances of a class.
        """
        return storage.all(cls)
