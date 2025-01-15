#!/usr/bin/python3
"""Command line interpreter"""
import cmd
import models
import shlex

class HBNBCommand(cmd.Cmd):
    """Class for the console, inheriting from cmd.Cmd"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)."""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            instance = models.dict_classes[args[0]]()
            instance.save()
            print(instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            obj = models.storage.all().get(instance_key)
            print(obj if obj else "** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and ID."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            if instance_key in models.storage.all():
                del models.storage.all()[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all instances of a class (or all if no class is provided)."""
        args = shlex.split(arg)
        if not args:
            for obj in models.storage.all().values():
                print(obj)
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in models.storage.all().items():
                if key.startswith(args[0]):
                    print(obj)

    def do_update(self, arg):
        """Update an instance based on class name and ID."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            obj = models.storage.all().get(instance_key)
            if obj:
                attr_name, attr_value = args[2], args[3].strip('"')
                try:
                    attr_value = eval(attr_value)  # Convert to correct type
                except (NameError, SyntaxError):
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()