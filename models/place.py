#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    """
    @classmethod
    def all(cls):
        """
        Return a dictionary with all instances of a class.
        """
        return storage.all(cls)
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
