#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """
    @classmethod
    def all(cls):
        """
        Return a dictionary with all instances of a class.
        """
        return storage.all(cls)
    name = ""
