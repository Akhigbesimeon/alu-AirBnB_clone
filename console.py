import cmd
import json
import os
import sys

# Ensure the models module can be imported correctly
try:
    sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
    from models import storage, BaseModel  # Import your storage system and BaseModel
except ModuleNotFoundError as e:
    raise ImportError("The 'models' module could not be found. Ensure it is located correctly.") from e

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
    }

    def do_create(self, arg):
        """Create a new instance of a class and save it."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[args[0]]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Show an instance of a class based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Destroy an instance of a class based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances of a class or all instances in general."""
        args = arg.split()
        objects = storage.all()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        instances = [str(obj) for key, obj in objects.items() if not args or key.startswith(args[0])]
        print(instances)

    def do_update(self, arg):
        """Update an instance based on class name, id, and attributes."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
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
        try:
            if '.' in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except ValueError:
            pass  # Leave as string if it can't be converted

        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
