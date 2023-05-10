#!/usr/bin/env python3
"""Defines Modules for the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines BaseClass HBNBCommand for the command interpreter"""
    
    prompt = '(hbnb)'
    
    def do_create(self, arg):
        """Creates a new instance of the command."""
        pass
    def do_quit(self):
        return True
        """Quits the command interpreter when called."""
    def do_show(self, arg):
        pass
    def do_destroy(self, arg):
        """Deletes an instance of the class."""
        pass
    def do_count(self, arg):
        """counts the number of instances of the classs"""
    
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()