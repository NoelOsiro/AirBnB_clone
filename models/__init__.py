#!/usr/bin/python3
"""Defines the BaseModel class."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
