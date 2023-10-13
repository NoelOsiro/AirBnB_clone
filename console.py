#!/usr/bin/python3
"""
Console module for the command interpreter.
"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def do_create(self, args):
        """Create a new instance of a class"""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on ID"""
        args_list = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args_list[0])
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args_list[0], args_list[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on ID"""
        args_list = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args_list[0])
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args_list[0], args_list[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances"""
        args_list = shlex.split(args)
        obj_list = []
        if not args:
            obj_list = [str(obj) for obj in storage.all().values()]
        else:
            try:
                cls = eval(args_list[0])
                obj_list = [str(obj) for obj in cls.all()]
            except NameError:
                print("** class doesn't exist **")
                return
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on ID and attribute name/value or dict"""
        args_list = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args_list[0])
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args_list[0], args_list[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
                return
            if len(args_list) < 3:
                print("** attribute name missing **")
                return
            if len(args_list) < 4:
                print("** value missing **")
                return
            attr_name = args_list[2]
            attr_value = args_list[3].strip('"')
            setattr(obj, attr_name, attr_value)
            storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_update_dict(self, args):
        """Updates an instance based on ID with a dictionary representation"""
        args_list = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args_list[0])
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args_list[0], args_list[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
                return
            if len(args_list) < 3:
                print("** dictionary missing **")
                return
            try:
                attr_dict = eval(args_list[2])
                if not isinstance(attr_dict, dict):
                    raise ValueError
                for attr, value in attr_dict.items():
                    setattr(obj, attr, value)
                storage.save()
            except (SyntaxError, ValueError):
                print("** invalid dictionary **")
        except NameError:
            print("** class doesn't exist **")

    def do_count(self, args):
        """Counts the number of instances of a class"""
        args_list = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = args_list[0]
            count = len(storage.all(cls))
            print(count)
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
