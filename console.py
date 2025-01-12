#!/usr/bin/python3
"""
Entry point of the command interpreter for the HBNB project.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command interpreter for the HBNB project. """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """ Quit command to exit the program. """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program. """
        print()
        return True

    def emptyline(self):
        """ Overrides the default behavior when an empty line is entered. """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
