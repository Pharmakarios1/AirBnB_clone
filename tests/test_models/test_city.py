#!/usr/bin/python3

"""Test for city model"""

from models.city import City
from datetime import datetime
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestCity(unittest.TestCase):
	"""
	Test cases for the City class
	"""

	def test_attributes(self):
		"""
		Test that the City class has the correct attributes
		"""
		city = City()
		self.assertTrue(hasattr(city, 'id'))
		self.assertTrue(hasattr(city, 'created_at'))
		self.assertTrue(hasattr(city, 'updated_at'))
		self.assertTrue(hasattr(city, 'state_id'))
		self.assertTrue(hasattr(city, 'name'))

	def test_state_id_attribute(self):
		"""
		Test that the state_id attribute is of type string and empty by defaul
		"""
		city = City()
		self.assertEqual(city.state_id, '')
		self.assertIsInstance(city.state_id, str)

	def test_name_attribute(self):
		"""
		Test that the name attribute is of type string and empty by default
		"""
		city = City()
		self.assertEqual(city.name, '')
		self.assertIsInstance(city.name, str)

	def test_str_representation(self):
		"""
		Test the __str__ method returns the expected string representation
		"""
		city = City()
		city_str = "[City] ({}) {}".format(city.id, city.__dict__)
		self.assertEqual(city_str, str(city))

	def test_to_dict_method(self):
		"""
		Test the to_dict method returns a dictionary representation of a City instance
		"""
		city = City()
		city_dict = city.to_dict()
		self.assertIsInstance(city_dict, dict)
		self.assertEqual(city_dict['__class__'], 'City')
		self.assertEqual(city_dict['state_id'], '')
		self.assertEqual(city_dict['name'], '')
		self.assertEqual(city_dict['id'], city.id)

if __name__ == '__main__':
    unittest.main()
