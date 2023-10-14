#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_new_instance(self):
        """
        Test creating a new instance of BaseModel.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertEqual(self.model.created_at, self.model.updated_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_init_with_kwargs(self):
        """
        Test initializing BaseModel with keyword arguments.
        """
        data = {
            'id': '12345',
            'created_at': '2023-10-10T12:00:00.000000',
            'updated_at': '2023-10-10T12:01:00.000000',
            'custom_attribute': 'custom_value'
        }
        model = BaseModel(**data)

        self.assertEqual(model.id, '12345')
        self.assertEqual(model.created_at.isoformat(), '2023-10-10T12:00:00')
        self.assertEqual(model.updated_at.isoformat(), '2023-10-10T12:01:00')
        self.assertEqual(model.custom_attribute, 'custom_value')

    def test_save_method(self):
        """
        Test the save method of BaseModel.
        """
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            model_dict['created_at'],
            self.model.created_at.isoformat()
            )
        self.assertEqual(
            model_dict['updated_at'],
            self.model.updated_at.isoformat()
            )

    def test_str_method(self):
        """
        Test the str method of BaseModel.
        """
        expected_str = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_new_instance_added_to_storage(self):
        """
        Test that a new instance is added to storage.
        """
        all_objs = storage.all()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], self.model)

    def test_id_type(self):
        """
        Test the type of the 'id' attribute.
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_updated_at_type(self):
        """
        Test the types of the 'created_at' and 'updated_at' attributes.
        """
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_updated_at_after_save(self):
        """
        Test that 'updated_at' changes after calling save().
        """
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        """
        Test that to_dict() returns a dictionary.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)


if __name__ == '__main__':
    unittest.main()
