#!/usr/bin/python3

"""
Entry point of the command interpreter for the HBNB project.
This module uses the cmd module to create an interactive shell.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """
    prompt = "(hbnb) "  # Custom prompt for the console
    classes = {"BaseModel": BaseModel}  # Supported classes

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to JSON, and prints the id.
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances or those of a specific class.
        Usage: all <class name> or all
        """
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.startswith(f"{args[0]}.")])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding/updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split(maxsplit=3)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                if attr_name not in ["id", "created_at", "updated_at"]:
                    try:
                        # Cast value to int, float, or keep it as a string
                        if attr_value.isdigit():
                            attr_value = int(attr_value)
                        elif '.' in attr_value:
                            attr_value = float(attr_value)
                    except ValueError:
                        pass
                    setattr(instance, attr_name, attr_value)
                    instance.save()

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        Usage: Press Ctrl+D
        """
        print()  # Print a newline for a clean exit
        return True

    def emptyline(self):
        """
        Overrides the default behavior when an empty line is entered.
        Does nothing.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
