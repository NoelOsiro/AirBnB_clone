#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittests for testing BaseModel class."""

    def setUp(self):
        """Set up the test environment."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Tear down the test environment."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_instantiation(self):
        """Test BaseModel instantiation and attributes."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIn(bm, models.storage.all().values())
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        bm2 = BaseModel()
        self.assertNotEqual(bm.id, bm2.id)
        self.assertLess(bm.created_at, bm2.created_at)
        self.assertLess(bm.updated_at, bm2.updated_at)

    def test_str_representation(self):
        """Test BaseModel string representation."""
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        dt_repr = repr(dt)
        self.assertIn("[BaseModel] (123456)", str(bm))
        self.assertIn("'id': '123456'", str(bm))
        self.assertIn("'created_at': " + dt_repr, str(bm))
        self.assertIn("'updated_at': " + dt_repr, str(bm)

    def test_instantiation_with_kwargs(self):
        """Test BaseModel instantiation with kwargs."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_save(self):
        """Test BaseModel save method."""
        bm = BaseModel()
        first_updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_save_updates_file(self):
        """Test if save method updates the JSON file."""
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_to_dict(self):
        """Test BaseModel to_dict method."""
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertEqual(tdict, bm.to_dict())

if __name__ == "__main__":
    unittest.main()
