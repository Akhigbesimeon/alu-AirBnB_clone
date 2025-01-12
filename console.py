#!/usr/bin/python3

"""
Entry point of the command interpreter for the HBNB project.
This module uses the cmd module to create an interactive shell.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """
    prompt = "(hbnb) "  # Custom prompt for the console

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

if _name_ == '_main_':
    HBNBCommand().cmdloop()