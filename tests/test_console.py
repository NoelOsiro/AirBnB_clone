import unittest
import os
import uuid
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

class TestPromptSymbol(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""
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
            HBNBCommand().onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        output = self.capture_stdout("")
        self.assertEqual("", output)

class TestExitCommands(unittest.TestCase):
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

    def test_quit_command(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_command(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

class TestHelpCommands(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def capture_stdout(self, command):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_help(self):
        output = self.capture_stdout("help")
        self.assertIn("Documented commands (type help <topic>):", output)
        self.assertIn( "EOF  all  count  create  destroy  help  quit  show  update  update_dict", output)

    def test_help_quit(self):
        output = self.capture_stdout("help quit")
        self.assertEqual(output, "Quit command to exit the program")

    def test_help_EOF(self):
            output = self.capture_stdout("help EOF")
            self.assertEqual(output, "EOF command to exit the program")

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
        self.assertEqual(output, "Updates an instance based on ID and attribute name/value or dict")

    def test_help_count(self):
        output = self.capture_stdout("help count")
        self.assertEqual(output, "Counts the number of instances of a class")

class TestCreateCommand(unittest.TestCase):
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
            HBNBCommand().onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_with_valid_class(self):
        output = self.capture_stdout("create BaseModel")
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** class name missing **")

    def test_create_with_nonexistent_class(self):
        output = self.capture_stdout("create NonExistentClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_without_class_name(self):
        output = self.capture_stdout("create")
        self.assertEqual(output, "** class name missing **")

    def test_create_and_check_in_storage(self):
        output = self.capture_stdout("create BaseModel")
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** class name missing **")
        instance_id = output
        created_instance = storage.all().get(f"BaseModel.{instance_id}")
        self.assertIsNotNone(created_instance)

    def test_create_and_check_string_representation(self):
        output = self.capture_stdout("create BaseModel")
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** class name missing **")
        instance_id = output
        created_instance = storage.all().get(f"BaseModel.{instance_id}")
        self.assertTrue(str(created_instance).startswith("[BaseModel]"))

class TestShowCommand(unittest.TestCase):
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
            HBNBCommand().onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_show_with_valid_class_and_id(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** instance id missing **")
        show_output = self.capture_stdout(f"show BaseModel {instance_id}")
        self.assertNotIn("** no instance found **", show_output)

    def test_show_with_nonexistent_class(self):
        output = self.capture_stdout("show NonExistentClass 12345")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_without_class_name(self):
        output = self.capture_stdout("show")
        self.assertEqual(output, "** class name missing **")

    def test_show_with_valid_class_and_nonexistent_id(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** instance id missing **")
        unique_non_existent_id = str(uuid.uuid4())
        show_output = self.capture_stdout(f"show BaseModel {unique_non_existent_id}")
        self.assertEqual(show_output, "** no instance found **")

    def test_show_with_valid_class_and_existing_instance(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** instance id missing **")
        show_output = self.capture_stdout(f"show BaseModel {instance_id}")
        self.assertNotEqual(show_output, "** no instance found **")

    def test_show_without_instance_id(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** instance id missing **")
        show_output = self.capture_stdout("show BaseModel")
        self.assertEqual(show_output, "** instance id missing **")

    def test_show_with_invalid_class(self):
        output = self.capture_stdout("show InvalidClass 12345")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_with_valid_class_and_nonexistent_instance(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        self.assertNotEqual(output, "** class doesn't exist **")
        self.assertNotEqual(output, "** instance id missing **")
        non_existent_id = str(uuid.uuid4())
        show_output = self.capture_stdout(f"show BaseModel {non_existent_id}")
        self.assertEqual(show_output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
