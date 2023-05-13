#!/usr/bin/env python3
"""Defines Modules for the entry point of the command interpreter"""

import cmd
import re
import json
from dateutil.parser import parse
from shlex import split
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines HolbertonBNB class that inherits from cmd module  for the command interpreter
    Attributes:
        prompt (str)--> the prompt string for the command.
    """
    
    prompt = "(hbnb)"
    
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    
    def do_create(self, arg):
        """Creates a new instance of the class and then print its id
        Usage--> create <classname>
        """
        
        date_object = parse(arg)
        if len(date_object) == 0:
            print("** class name missing **")
        elif date_object[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(date_object[0])().id)
            storage.save()
        
   
    def do_show(self, arg):
        """This displays the string representation of the class.
        Usage:--> show <class name> <id> or <classname>.show(<id>)
        """
        date_object = parse(arg)
        objdict = storage.all()
        if len(date_object) == 0:
            print("** class name missing **")
        elif date_object[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(date_object) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(date_object[0], date_object[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(date_object[0], date_object[1])])

    def do_destroy(self, arg):
        """Deletes an instance of the class."""
        date_object = parse(arg)
        objdict = storage.all()
        if len(date_object) == 0:
            print("** class name missing **")
        elif date_object[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(date_object) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(date_object[0], date_object[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(date_object[0], date_object[1])]
            storage.save()
    def do_count(self, arg):
        """counts or retrive the number of instances of the classs
        Usage--> count <classname> or <classname>.count()
        """
        date_object = parse(arg)
        count = 0
        for obj in storage.all().values():
            if date_object[0] == obj.__class__.__name__:
                count += 1
        print(count)

        
    def do_update(self, arg):
        """updates an instance of the class by adding attributes to it
        Usage--> update <class> <id> <attribute_name> <attribute_value>
        """
        date_object = parse(arg)
        objdict = storage.all()

        if len(date_object) == 0:
            print("** class name missing **")
            return False
        if date_object[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(date_object) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(date_object[0], date_object[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(date_object) == 2:
            print("** attribute name missing **")
            return False
        if len(date_object) == 3:
            try:
                type(eval(date_object[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(date_object) == 4:
            obj = objdict["{}.{}".format(date_object[0], date_object[1])]
            if date_object[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[date_object[2]])
                obj.__dict__[date_object[2]] = valtype(date_object[3])
            else:
                obj.__dict__[date_object[2]] = date_object[3]
        elif type(eval(date_object[2])) == dict:
            obj = objdict["{}.{}".format(date_object[0], date_object[1])]
            for k, v in eval(date_object[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()
    def do_all(self, arg):
        """prints all instances of the class in string format
        Usage--> all <classname> or <classname>.all()
        """
        date_object = parse(arg)
        if len(date_object) > 0 and date_object[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(date_object) > 0 and date_object[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(date_object) == 0:
                    objl.append(obj.__str__())
            print(objl)
        
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
        """Returns to default if nothing was specified or invalid"""
        
        arg_command_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_command_dict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return arg_command_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
        
        
      
if __name__ == '__main__':
    HBNBCommand().cmdloop()


