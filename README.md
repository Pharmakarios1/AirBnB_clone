# AirBNB_Clone
![AirBNB_clone](https://www.octoproperty.com/wp-content/uploads/2021/12/airbnb-678x381-1.jpeg)<hr>
# Project Description

This first aspect of AirBNB project involves the use of Object-Oriented Programming (OOP) to develop a backend for the web application and with the help of python cmd module to develop a console interface that respond to commands used in interacting with the web App. 

The storage facility built for this aspect is based on the ability of python to easily store data in a lightweight file called json file through the help of json module.

The analysis are: 

Instances or python objects created are converted to python data structure and stored in json file through serialization.<br>Instances --> pds--> json file (serialization)<br>In like manner, for easy retrieval system, the json strings stored are converted to python data structure and then to the instance or object through deserialization.<br>json file --> pds --> instances (Deserialization)<hr>
![storage](https://hazelcast.com/wp-content/uploads/2021/12/serialization-deserialization-diagram-800x318-1.png)
# Description of the command line interface (Cli)/ interpreter
The command line interface is similar to the borne-again shell (Bash shell), However, it is laced with a limited number of commands solely for the purpose of the project (AirBnb_clone WebApp)<br>

The command line interpreter interface is implemented to serve as the frontend part of the web application. The clients or users can through the commands interacts with the backend.

The commands available are:<br>
    * show<br>
    * create<br>
    * update<br>
    * destroy<br>
    * count<br>
This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

# What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:<br>

Create a new object (ex: a new User or a new Place)<br>
Retrieve an object from a file, a database etc…<br>
Do operations on objects (count, compute stats, etc…)<br>
Update attributes of an object<br>
Destroy an object<hr>
# Snippet of commands usage
        
    * create helps to create a new instance (A user may create a new account)
    * show commands may help to retrieve an object from a file, a database from the console
    * update commands helps to update attributes of an object stored.
    * destroy helps to delete an object
    * count and show helps in doing important operations from the command interpreter.


# How to invoke and start the program
Instructions below will help to get the program running on your local machine with all of it's dependencies for testing and further developments.

install by git cloning this repository<hr>

        http://github.com/pharmakarios1/AirBnB_clone.git

After cloning, you should have a directory named AirBnB_clone on your local machine. Within the directory is contained all files that allow the program to run.

# Files in the cloned directory:
1. Authors: This list the contributing individuals fo this project
2. tests: This is a sub-directory containing the test carried out for the project mainly for edge cases, and quality assurance.
3. console.py: This is the main python executable file that provides the environment from which commands are issued to the console to effect a certain action.
4. models: is a sub-directory containing a host of files:

----> models/engine/file_storage.py: This is a class that serializes objects to a json file and in-turn deserializes them back into object instances when commands are issued.<br>
---->models/__init__.py: This is a magic file. it is very essential for the build up of the FileStorage.<br>
---->models/base_model.py: Class that defines all common attributes and methods for other classes<br>
---->models/user.py: This file is the User class that inherits from the BaseModel.<br>
---->models/state.py: This file is the state class that inherits from the BaseModel.<br>
---->models/city.py: This file is the city class that inherits from the BaseModel.<br>
---->models/amenity.py: This file is the amenity class that inherits from the BaseModel.<br>
---->models/place.py: This file is the place class that inherits from the BaseModel.<br>
---->models/review.py: This file is the review class that inherits from the BaseModel.

<hr>

# Execution:
Usage is in two unique modes:<br> 
        1. Interactive mode <br>
        2. Non-interactive mode <br>

# Interactive mode
the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.
        $ ./console.py
        (hbnb) help

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit

        (hbnb) 
        (hbnb) 
        (hbnb) quit
        $

# Non-Interactive mode
the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.

        $ echo "help" | ./console.py
        (hbnb)

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit
        (hbnb) 
        $
        $ cat test_help
        help
        $
        $ cat test_help | ./console.py
        (hbnb)

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit
        (hbnb) 
        $

# Inputing and Executing commands:
The interactive mode accepts commands from the keyboard when the prompt (hbnb) appears in the console. This command(s) are then executed when the return key[ENTER] is hit. On execution, the console will process it and then present an output which could be the needed retrieval, or error display which is then exited by a combination of keys: "Ctrl+ C", "Ctrl+D", "quit" or "EOF"

On the other hand, to achieve same result, the command(s) will have to be piped through an echo command.
         $ echo "help" | ./console.py

# Arguments:

Like most other commands, options like flags or plain text could be passed to the console to execute the needed output. the console shell recognizes these options when a separated by a single space.

        user@Pharmakarios MINGW64 ~/Desktop/AirBnB_clone (main)
        ./console.py
        (hbnb) create BaseModel
        32d2ff7a-96c1-a11f-80b3-63732d6e7883
       user@Pharmakarios MINGW64 ~/Desktop/AirBnB_clone (main)
       ./console.py

# Commands and usage: <hr>

        
   Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

# help command
This command is built inside the cmd module and it helps to list all available commands:
           Documented commands (type help <topic>):
========================================
EOF  count  create  destroy  help

Undocumented commands:
======================
quit  show     

# Unittests 
Unittests for the for this project are defined in the [tests](./tests)
directory. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```
<hr>

# pharmakarios1 (Blessed Akhigbe)
![Pharmakarios1](https://avatars.githubusercontent.com/u/89057471?v=4)

# nnejiobioma (Johnson Johnson)
![nnejiobioma](https://avatars.githubusercontent.com/u/59613857?v=4)
