import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def capture_stdout(self, command):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_help(self):
        output = self.capture_stdout("help")
        print(output)
        self.assertIn("Documented commands (type help <topic>):", output)
        self.assertIn("EOF  help  quit  create  show  destroy  all  update", output)

    def test_help_quit(self):
        output = self.capture_stdout("help quit")
        self.assertEqual(output, "Quit command to exit the program")

    def test_help_create(self):
        output = self.capture_stdout("help create")
        self.assertEqual(output, "Create a new instance of BaseModel")

    def test_help_show(self):
        output = self.capture_stdout("help show")
        self.assertEqual(output, "Prints the string representation of an instance based on ID")

    def test_help_destroy(self):
        output = self.capture_stdout("help destroy")
        self.assertEqual(output, "Deletes an instance based on ID")

    def test_help_all(self):
        output = self.capture_stdout("help all")
        self.assertEqual(output, "Prints all string representation of all instances")

    def test_help_update(self):
        output = self.capture_stdout("help update")
        self.assertEqual(output, "Updates an instance based on ID and attribute name/value or dictionary")

    def test_help_count(self):
        output = self.capture_stdout("help count")
        self.assertEqual(output, "Counts the number of instances of a class")

    def test_quit_command(self):
        with self.assertRaises(SystemExit) as e:
            self.console.onecmd("quit")
        self.assertEqual(e.exception.code, None)

    def test_EOF_command(self):
        with self.assertRaises(SystemExit) as e:
            self.console.onecmd("EOF")
        self.assertEqual(e.exception.code, None)

    def test_create_command(self):
        output = self.capture_stdout("create BaseModel")
        self.assertTrue(len(output) == 36)
        self.assertTrue(isinstance(storage.all()["BaseModel." + output], BaseModel))

    def test_create_command_missing_class(self):
        output = self.capture_stdout("create")
        self.assertEqual(output, "** class name missing **")

    def test_create_command_invalid_class(self):
        output = self.capture_stdout("create InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_command(self):
        bm = BaseModel()
        output = self.capture_stdout(f"show BaseModel {bm.id}")
        self.assertIn(f"[BaseModel] ({bm.id})", output)

    def test_show_command_missing_class(self):
        output = self.capture_stdout("show")
        self.assertEqual(output, "** class name missing **")

    def test_show_command_invalid_class(self):
        output = self.capture_stdout("show InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_command_missing_id(self):
        output = self.capture_stdout("show BaseModel")
        self.assertEqual(output, "** instance id missing **")

    def test_show_command_invalid_id(self):
        output = self.capture_stdout("show BaseModel 1234")
        self.assertEqual(output, "** no instance found **")

    def test_destroy_command(self):
        bm = BaseModel()
        bm_id = bm.id
        output = self.capture_stdout(f"destroy BaseModel {bm_id}")
        self.assertNotIn(f"{bm_id}", storage.all())

    def test_destroy_command_missing_class(self):
        output = self.capture_stdout("destroy")
        self.assertEqual(output, "** class name missing **")

    def test_destroy_command_invalid_class(self):
        output = self.capture_stdout("destroy InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command_missing_id(self):
        output = self.capture_stdout("destroy BaseModel")
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_command_invalid_id(self):
        output = self.capture_stdout("destroy BaseModel 1234")
        self.assertEqual(output, "** no instance found **")

    def test_all_command(self):
        bm = BaseModel()
        output = self.capture_stdout("all")
        self.assertIn(f"[BaseModel] ({bm.id})", output)

    def test_all_command_with_class(self):
        bm = BaseModel()
        output = self.capture_stdout("all BaseModel")
        self.assertIn(f"[BaseModel] ({bm.id})", output)

    def test_all_command_invalid_class(self):
        output = self.capture_stdout("all InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_command(self):
        bm = BaseModel()
        bm_id = bm.id
        output = self.capture_stdout(f"update BaseModel {bm_id} name 'New Name'")
        self.assertEqual(bm.name, 'New Name')

    def test_update_command_missing_class(self):
        output = self.capture_stdout("update")
        self.assertEqual(output, "** class name missing **")

    def test_update_command_invalid_class(self):
        output = self.capture_stdout("update InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_command_missing_id(self):
        output = self.capture_stdout("update BaseModel")
        self.assertEqual(output, "** instance id missing **")

    def test_update_command_invalid_id(self):
        output = self.capture_stdout("update BaseModel 1234")
        self.assertEqual(output, "** no instance found **")

    def test_update_command_missing_attr_name(self):
        bm = BaseModel()
        bm_id = bm.id
        output = self.capture_stdout(f"update BaseModel {bm_id}")
        self.assertEqual(output, "** attribute name missing **")

    def test_update_command_missing_attr_value(self):
        bm = BaseModel()
        bm_id = bm.id
        output = self.capture_stdout(f"update BaseModel {bm_id} name")
        self.assertEqual(output, "** value missing **")

    def test_update_dict_command(self):
        bm = BaseModel()
        bm_id = bm.id
        output = self.capture_stdout(f"update_dict BaseModel {bm_id} {{'name': 'Updated Name'}}")
        self.assertEqual(bm.name, 'Updated Name')

    def test_update_dict_command_missing_class(self):
        output = self.capture_stdout("update_dict")
        self.assertEqual(output, "** class name missing **")

    def test_update_dict_command_invalid_class(self):
        output = self.capture_stdout("update_dict InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_dict_command_missing_id(self):
        output = self.capture_stdout("update_dict BaseModel")
        self.assertEqual(output, "** instance id missing **")

    def test_update_dict_command_invalid_id(self):
        output = self.capture_stdout("update_dict BaseModel 1234")
        self.assertEqual(output, "** no instance found **")

    def test_update_dict_command_missing_dict(self):
        bm = BaseModel()
        bm_id = bm.id
        output = self.capture_stdout(f"update_dict BaseModel {bm_id}")
        self.assertEqual(output, "** dictionary missing **")

    def test_update_dict_command_invalid_dict(self):
        bm = BaseModel()
        bm_id = bm.id
        output = self.capture_stdout(f"update_dict BaseModel {bm_id} 'invalid_dict'")
        self.assertEqual(output, "** invalid dictionary **")

    def test_count_command(self):
        bm = BaseModel()
        output = self.capture_stdout("count BaseModel")
        self.assertEqual(output, "1")

    def test_count_command_missing_class(self):
        output = self.capture_stdout("count")
        self.assertEqual(output, "** class name missing **")

    def test_count_command_invalid_class(self):
        output = self.capture_stdout("count InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_user_command(self):
        output = self.capture_stdout("create User")
        self.assertTrue(len(output) == 36)
        self.assertTrue(isinstance(storage.all()["User." + output], User))

    def test_create_state_command(self):
        output = self.capture_stdout("create State")
        self.assertTrue(len(output) == 36)
        self.assertTrue(isinstance(storage.all()["State." + output], State))

    def test_create_city_command(self):
        output = self.capture_stdout("create City")
        self.assertTrue(len(output) == 36)
        self.assertTrue(isinstance(storage.all()["City." + output], City))

    def test_create_amenity_command(self):
        output = self.capture_stdout("create Amenity")
        self.assertTrue(len(output) == 36)
        self.assertTrue(isinstance(storage.all()["Amenity." + output], Amenity))

    def test_create_place_command(self):
        output = self.capture_stdout("create Place")
        self.assertTrue(len(output) == 36)
        self.assertTrue(isinstance(storage.all()["Place." + output], Place))

    def test_create_review_command(self):
        output = self.capture_stdout("create Review")
        self.assertTrue(len(output) == 36)
        self.assertTrue(isinstance(storage.all()["Review." + output], Review))


if __name__ == '__main__':
    unittest.main()
