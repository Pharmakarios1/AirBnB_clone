#!/usr/bin/env python3
"""Defines Modules for the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines BaseClass HBNBCommand for the command interpreter"""
    
    prompt = '(hbnb)'
    
    
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()