#!/usr/bin/python3

"""
This is a base class for other models. It provides funtionality that can be used by other models
In this instance BaseModel class id defined the will be called from the init function and other functions
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
	""" Base Class created with uuid4. Each value containing a unique id for each base models"""
	import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            self.id = str(self.id)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

