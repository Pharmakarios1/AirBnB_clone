#!//usr/bin/python3
"""
Taset case for amenities
"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
	def setUp(self):
		self.amenity = Amenity()

	def test_instance_creation(self):
		self.assertIsInstance(self.amenity, Amenity)
        	self.assertIsInstance(self.amenity, BaseModel)

	def test_attributes(self):
		self.assertTrue(hasattr(self.amenity, "name"))
		self.assertEqual(self.amenity.name, "")
		self.assertTrue(hasattr(self.amenity, "id"))
		self.assertTrue(hasattr(self.amenity, "created_at"))
		self.assertTrue(hasattr(self.amenity, "updated_at"))

	def test_str_method(self):
		string = str(self.amenity)
		self.assertEqual(string, "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.to_dict()))

	def test_to_dict_method(self):
		amenity_dict = self.amenity.to_dict()
		self.assertTrue(type(amenity_dict) is dict)
		self.assertEqual(amenity_dict['__class__'], "Amenity")
		self.assertEqual(type(amenity_dict['created_at']), str)
		self.assertEqual(type(amenity_dict['updated_at']), str)
