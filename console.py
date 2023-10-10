#!/usr/bin/python3
"""
Console module for the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Empty line does nothing.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it (to the JSON file), and print the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not on the class name.
        """
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    instance = objects[key]
                    setattr(instance, args[2], args[3])
                    instance.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
