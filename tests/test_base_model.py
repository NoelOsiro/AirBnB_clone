import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_new_instance(self):
        """
        Test creating a new instance of BaseModel.
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertEqual(model.created_at, model.updated_at)
        self.assertIsInstance(model.created_at, datetime)

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
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(prev_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_str_method(self):
        """
        Test the str method of BaseModel.
        """
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_new_instance_added_to_storage(self):
        """
        Test that a new instance is added to storage.
        """
        model = BaseModel()
        all_objs = storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], model)

if __name__ == '__main__':
    unittest.main()
