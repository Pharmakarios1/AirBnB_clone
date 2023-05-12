#!/usr?bin/python3

from models.base_model import BaseModel

"""
This is used to create a user account on the program which is 
then stored in Storage_file
"""

class User(BaseModel):
	"""
	This creates a new user account.
	It also provides the fields that is needed with the followng attribues:

	email: str
        	The email of the User.
    	password: str
        	The password of the User.
    	first_name: str
        	The first name of the User.
    	last_name: str
        	The last name of the User.
	"""

	email = ""
	password = ""
	first_name = ""
	last_name = ""

def
