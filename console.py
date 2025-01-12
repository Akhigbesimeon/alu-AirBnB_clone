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
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel
    }

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class name>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based on the class name.
        Usage: all <class name> or all
        """
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in storage.all().items() if key.startswith(class_name)])

    def do_update(self, arg):
        """
        Updates an instance based on class name and id by adding/updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        obj = storage.all()[key]
        # Skip updating protected attributes
        if attr_name not in ("id", "created_at", "updated_at"):
            try:
                attr_value = eval(attr_value)  # Cast to correct type
            except (NameError, SyntaxError):
                pass
            setattr(obj, attr_name, attr_value)
            obj.save()

    def emptyline(self):
        """
        Overrides the default behavior when an empty line is entered.
        Does nothing.
        """
        pass

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
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
