#!/usr/bin/env python3
"""Defines Modules for the entry point of the command interpreter"""

import cmd
import re
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines BaseClass HBNBCommand for the command interpreter"""
    
    prompt = "(hbnb)"
    
    def do_create(self, arg):
        """Creates a new instance of the class."""
        pass
   
    def do_show(self, arg):
        pass
    def do_destroy(self, arg):
        """Deletes an instance of the class."""
        pass
    def do_count(self, arg):
        """counts the number of instances of the classs"""
        pass
    def do_update(self, arg):
        """updates an instance of the class by adding attributes to it"""
        pass
    def do_all(self, arg):
        """prints all instances of the class in string format"""
        pass
        
    def do_quit(self):
        return True
        """Quits the command interpreter when called."""
        
        
    def do_EOF(self, arg):
        """The function takes care of the End of file"""
        return True
    
    def do_emptyline(sefl):
        """Function is inactive and does nothing when Enter is entered"""
        pass
    
    def default(self, arg):
        """Returns to default if nothing was specified"""
        
        
      
if __name__ == '__main__':
    HBNBCommand().cmdloop()

