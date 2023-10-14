#!/usr/bin/python3
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
    """Tests for exit commands: quit and EOF."""

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
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_quit_command(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_command(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

class TestHelpCommands(unittest.TestCase):
    """Tests for help commands."""

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
        self.assertIn("EOF  all  count  create  destroy  help  quit  show  update", output)

    def test_help_quit(self):
        output = self.capture_stdout("help quit")
        self.assertEqual(output, "Quit command to exit the program")

    def test_help_EOF(self):
        output = self.capture_stdout("help EOF")
        self.assertEqual(output, "EOF command to exit the program")

    def test_help_create(self):
        output = self.capture_stdout("help create")
        self.assertEqual(output, "Create a new instance of a class")

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
    """Tests for the create command."""

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
        assert "** class doesn't exist **" not in output
        assert "** class name missing **" not in output
        assert output  # Ensure that output is not empty

    def test_create_with_nonexistent_class(self):
        output = self.capture_stdout("create NonExistentClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_without_class_name(self):
        output = self.capture_stdout("create")
        self.assertEqual(output, "** class name missing **")

    def test_create_and_check_in_storage(self):
        """Test creating a valid object and checking if it's in storage"""
        output = self.capture_stdout("create BaseModel")
        created_instance_id = output.strip()
        created_instance = storage.all()["BaseModel.{}".format(created_instance_id)]
        assert created_instance is not None  # Check if created_instance is not None


    def test_create_and_check_string_representation(self):
        output = self.capture_stdout("create BaseModel")
        assert "** class doesn't exist **" not in output
        assert "** class name missing **" not in output
        instance_id = output
        created_instance = storage.all().get(f"BaseModel.{instance_id}")
        assert str(created_instance).startswith("[BaseModel]")

    def test_create_with_invalid_json_format(self):
        output = self.capture_stdout('create BaseModel {"invalid_key": "invalid_value"}')
        self.assertEqual(output, "** invalid dictionary **")

class TestShowCommand(unittest.TestCase):
    """Tests for the show command."""

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
        create_output = self.capture_stdout("create BaseModel")
        instance_id = create_output.strip('[]').split(',')[0].strip().strip('\'')
        command = f"show BaseModel {instance_id}"
        show_output = self.capture_stdout(command)
        assert "** class doesn't exist **" not in show_output
        assert "** no instance found **" not in show_output
        obj = storage.all()["BaseModel.{}".format(instance_id)]
        self.assertEqual(obj.__str__(), show_output)



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
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        unique_non_existent_id = str(uuid.uuid4())
        show_output = self.capture_stdout(f"show BaseModel {unique_non_existent_id}")
        self.assertEqual(show_output, "** no instance found **")

    def test_show_with_valid_class_and_existing_instance(self):
        create_output = self.capture_stdout("create BaseModel")
        instance_id = create_output.strip('[]').split(',')[0].strip().strip('\'')
        command = f"show BaseModel {instance_id}"
        show_output = self.capture_stdout(command)
        assert "** class doesn't exist **" not in show_output
        assert "** no instance found **" not in show_output
        obj = storage.all()["BaseModel.{}".format(instance_id)]
        self.assertEqual(obj.__str__(), show_output)


    def test_show_without_instance_id(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        show_output = self.capture_stdout("show BaseModel")
        self.assertEqual(show_output, "** instance id missing **")

    def test_show_with_invalid_class(self):
        output = self.capture_stdout("show InvalidClass 12345")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_with_valid_class_and_nonexistent_instance(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        non_existent_id = str(uuid.uuid4())
        show_output = self.capture_stdout(f"show BaseModel {non_existent_id}")
        self.assertEqual(show_output, "** no instance found **")

class TestDestroyCommand(unittest.TestCase):
    """Tests for the destroy command."""

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

    def test_destroy_with_valid_class_and_existing_instance(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        destroy_output = self.capture_stdout(f"destroy BaseModel {instance_id}")
        show_output = self.capture_stdout(f"show BaseModel {instance_id}")
        self.assertEqual(show_output, "** no instance found **")

    def test_destroy_without_instance_id(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        destroy_output = self.capture_stdout("destroy BaseModel")
        self.assertEqual(destroy_output, "** instance id missing **")

    def test_destroy_with_invalid_class(self):
        output = self.capture_stdout("destroy InvalidClass 12345")
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_with_valid_class_and_nonexistent_instance(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        non_existent_id = str(uuid.uuid4())
        destroy_output = self.capture_stdout(f"destroy BaseModel {non_existent_id}")
        self.assertEqual(destroy_output, "** no instance found **")

    def test_destroy_with_valid_class_and_existing_instance_twice(self):
        self.capture_stdout("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        instance_id = output.strip('[]').split(',')[0].strip().strip('\'')
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        destroy_output = self.capture_stdout(f"destroy BaseModel {instance_id}")
        destroy_output = self.capture_stdout(f"destroy BaseModel {instance_id}")
        self.assertEqual(destroy_output, "** no instance found **")

class TestCountCommand(unittest.TestCase):
    """Tests for the count command."""

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

    def test_count_existing_class(self):
        output = self.capture_stdout("count BaseModel")
        assert "** class doesn't exist **" not in output
        assert "** class name missing **" not in output
        assert output.isdigit()

    def test_count_non_existing_class(self):
        output = self.capture_stdout("count MyModel")
        self.assertEqual(output, "** class doesn't exist **")

    def test_count_missing_class_name(self):
        output = self.capture_stdout("count")
        self.assertEqual(output, "** class name missing **")

class TestUpdateCommands(unittest.TestCase):
    """Tests for the update commands."""

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

    def test_update_existing_instance(self):
        output = self.capture_stdout("create BaseModel")
        instance_id = output
        output = self.capture_stdout(f"update BaseModel {instance_id} name 'NewName'")
        assert "** class doesn't exist **" not in output
        assert "** class name missing **" not in output
        assert "** instance id missing **" not in output
        assert "** attribute name missing **" not in output
        assert "** value missing **" not in output

    def test_update_non_existing_instance(self):
        output = self.capture_stdout("update BaseModel NonExistentID name 'NewName'")
        self.assertEqual(output, "** no instance found **")

    def test_update_missing_class_name(self):
        output = self.capture_stdout("update NonExistentClass NonExistentID name 'NewName'")
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_instance_id(self):
        output = self.capture_stdout("update BaseModel")
        self.assertEqual(output, "** instance id missing **")

    def test_update_missing_attribute_name(self):
        instance_id = self.capture_stdout("create BaseModel")
        obj = storage.all()["BaseModel.{}".format(instance_id)]
        output = self.capture_stdout(f"update BaseModel {instance_id}")
        self.assertEqual(output, "** attribute name missing **")

    def test_update_missing_new_value(self):
        instance_id = self.capture_stdout("create BaseModel")
        obj = storage.all()["BaseModel.{}".format(instance_id)]
        output = self.capture_stdout(f"update BaseModel {instance_id} name")
        self.assertEqual(output, "** value missing **")

    def test_update_invalid_json_format(self):
        instance_id = self.capture_stdout("create BaseModel")
        obj = storage.all()["BaseModel.{}".format(instance_id)]
        show_output = self.capture_stdout(f"update BaseModel {instance_id} name {'invalidJSON'}")
        self.assertEqual(show_output, "** invalid dictionary **")


    def test_update_with_dictionary(self):
        output = self.capture_stdout("update BaseModel ExistingID {'name': 'NewName', 'age': 30}")
        assert "** class doesn't exist **" not in output
        assert "** instance id missing **" not in output
        assert "** invalid dictionary **" not in output

    def test_update_non_existing_class(self):
        output = self.capture_stdout("update NonExistentClass ExistingID name 'NewName'")
        self.assertEqual(output, "** class doesn't exist **")

class TestConsoleCity(unittest.TestCase):
    
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

    def test_create_city(self):
        """Test creating a new City instance using the console."""
        instance_id = self.capture_stdout("create City")
        self.assertFalse(HBNBCommand().onecmd("create City"))
        self.assertLess(0, len(instance_id))
        testKey = "City.{}".format(instance_id)
        self.assertIn(testKey, storage.all().keys())

    def test_show_city(self):
        """Test displaying a City instance using the console."""
        instance_id = self.capture_stdout("create City")
        output = self.capture_stdout(f"show City {instance_id}")
        self.assertTrue(str(instance_id) in output)

    def test_destroy_city(self):
        """Test destroying a City instance using the console."""
        instance_id = self.capture_stdout("create City")
        output = self.capture_stdout(f"destroy  City {instance_id}")
        city_key = f"City.{instance_id}"
        self.assertIsNone(storage.all(City).get(city_key))

if __name__ == '__main__':
    unittest.main()
