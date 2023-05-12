#!/usr/bin/python3
 from models.base_model import BaseModel

"""
This is the BaseModel for review
"""
class Review(BaseModel):
	"""
	This is the public class attributes foe review

	Attributes are :
	place_id: string - empty string: it will be the Place.id
	user_id: string - empty string: it will be the User.id
	text: string - empty string
	"""
	place_id = ""
	user_id = ""
	text = ""	
