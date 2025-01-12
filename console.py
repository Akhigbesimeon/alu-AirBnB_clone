import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        if args not in storage.classes():
            print("** class doesn't exist **")
            return
        instance = storage.classes()[args]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Shows the string representation of an instance"""
        tokens = args.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, args):
        """Deletes an instance"""
        tokens = args.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Prints all string representations of all instances"""
        if args and args not in storage.classes():
            print("** class doesn't exist **")
            return
        instances = []
        for obj in storage.all().values():
            if not args or obj.__class__.__name__ == args:
                instances.append(str(obj))
        print(instances)

    def do_update(self, args):
        """Updates an instance"""
        tokens = args.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(tokens) < 3:
            print("** attribute name missing **")
            return
        if len(tokens) < 4:
            print("** value missing **")
            return
        attr_name = tokens[2]
        attr_value = tokens[3].strip('"')

        # Convert value to appropriate type
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            attr_value = attr_type(attr_value)
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program with EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
