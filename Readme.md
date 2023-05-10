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


