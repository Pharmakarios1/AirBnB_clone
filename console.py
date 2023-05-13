#!/usr/bin/env python3
"""Defines Modules for the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines HolbertonBNB class that inherits from cmd module  for the command interpreter
    Attributes:
        prompt (str)--> the prompt string for the command.
    """
    
    prompt = "(hbnb):  "
    
    def do_quit(self):
        """Quit command to exit the command interpreter"""
        return True
    def do_EOF(self):
        """End of file: exit the command interpreter"""
        return True
    
    

    
    
   
        
      
if __name__ == '__main__':
    HBNBCommand().cmdloop()


