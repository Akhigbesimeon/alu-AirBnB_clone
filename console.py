#!/usr/bin/python3
"""command line interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """class for the console, inheriting from cmd.Cmd"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """command for exiting the program."""
        return True

    def do_EOF(self, arg):
        """Exiting the program with EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Doing nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                instance = models.dict_classes[arg]()
                instance.save()
                print(instance.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = args[0] + "." + args[1]
            if instance_key in models.storage.all():
                print(models.storage.all()[instance_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = args[0] + "." + args[1]
            if instance_key in models.storage.all():
                del models.storage.all()[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Shows all instances"""
        args = arg.split()
        if not arg:
            for value in models.storage.all().values():
                print(str(value))
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()
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
            instance_key = args[0] + "." + args[1]
            if instance_key in models.storage.all():
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(
                    models.storage.all()[instance_key], attr_name, attr_value)
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()