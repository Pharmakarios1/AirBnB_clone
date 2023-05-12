#!/usr/bin/python3

from models.base_model import BaseModel

"""
This is the city class baseModel for the project
"""
class City(BaseModel):
	"""
	This is the city class:

	It has the following attributes:
	state_id: string - empty string: it will be the State.id
	name: string - empty string
	"""
	state_id = ""
	name = ""	
