import unittest
import pycodestyle
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_pep8_conformance(self):
        """
        Test that the code complies with PEP 8.
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "PEP 8 style issues found")

    def test_base_model_attributes(self):
        """
        Test the attributes of the BaseModel instance.
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_base_model_id(self):
        """
        Test the uniqueness of the 'id' attribute.
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_base_model_created_at_updated_at(self):
        """
        Test the 'created_at' and 'updated_at' attributes.
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_base_model_save(self):
        """
        Test the 'save' method.
        """
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(prev_updated_at, model.updated_at)

    def test_base_model_to_dict(self):
        """
        Test the 'to_dict' method.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_base_model_str(self):
        """
        Test the '__str__' method.
        """
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_base_model_init_from_dict(self):
        """
        Test initializing BaseModel from a dictionary representation.
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

if __name__ == '__main__':
    unittest.main()
