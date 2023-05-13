#!/usr/bin/env python3
"""Defines Modules for the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines HolbertonBNB class that inherits from cmd module  for the command interpreter
    Attributes:
        prompt (str)--> the prompt string for the command.
    """
    
    prompt = "(hbnb):  "
    
    

    
    
   
        
      
if __name__ == '__main__':
    HBNBCommand().cmdloop()


