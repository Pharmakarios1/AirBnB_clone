#!/usr/bin/python3

"""
This is a base class for other models.
It provides funtionality that can be used by other models
In this instance BaseModel class id defined the will be called from the init function and other functions
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""This is is the BaseModel of the project. which other class and instances will read from"""

	def __init__(self, *args, **kwargs):
		"""This helps to initialize BaseModel."""

		if kwargs:
			for key, value in kwargs.items():
				if key == 'created_at' or key == 'updated_at':
					value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
				setattr(self, key, value)
		else:
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)
	def save(self):
		"""
		This helps to update the current time of the base model
		datetime.now is used instead of datetime.today.
		reason being that the now will give the current
		date as of the date of execution.
		"""
		self.update_at = datetime.now()
		models.storage.save()
		
	def to_dict(self):
		"""
		This returns the dictionary of Base Model in the project
		"""
		d = self.__dict__.copy()
		d['__class__'] = self.__class__.__name__
		d['created_at'] = self.created_at.isoformat()
		d['updated_at'] = self.updated_at.isoformat()
		return d

	def __str__(self):
		"""print representation of the BaseModel instance."""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())
