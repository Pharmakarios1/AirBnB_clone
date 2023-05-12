#!/usr/bin/python3
""" A class FileStorage that serializes instances to a JSON file and 
deserializes JSON file to instances: 
"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
	"""
	This is the file storage engine part 
	that will store to JASON file (ex: file.jason).
	Creates an object __object dictionary that will store all
	objects by <class name>.id
	"""
	
	__file_path = "file.json"
	__objects = {}

	def all(self):
                """ Return dictionary of all __objects stored """
                return FileStorage.__objects

	def new(self, obj):
        	""" 
		This is the __objects dictionary that will store.
		all objects by <class name>.id
		"""
        	key = obj.__class__.__name__ + "." + obj.id
        	FileStorage.__objects[key] = obj

	def save(self):
		"""
		serializes __objects to the JSON file (path: __file_path)
		"""
		json_dict = {}
		for key, val in FileStorage.__objects.items():
			json_dict[key] = val.to_dict()
		with open(FileStorage.__file_path, "w", encoding="utf-8") as d:
			json.dump(json_dict, d)

	def reload(self):
        	""" Deserialize JSON file __file_path if it exists, If it does not exist exit the program or pass """
        	if os.path.exists(FileStorage.__file_path):
            		with open(FileStorage.__file_path, encoding="utf-8") as d:
                		json_dict = json.load(d)
                		for key, val in json_dict.items():
                    			class_name = val['__class__']
                    			if class_name in globals():
                        			obj = globals()[class_name](**val)
                        			FileStorage.__objects[key] = obj

	except FileNotFoundError:
		pass
