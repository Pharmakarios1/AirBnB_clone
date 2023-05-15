#!/usr/bin/python3
"""
Test for user model.
"""

from models.user import User
import unittest
import 

class TestUser(unittest.TestCase):
	"""
	User model class for User test
	"""
	def test_user_instance(self):
		z = User()
		self.assertIsInstance(z, User)
	

	def test_user_attributes(self):
		z = User()
		self.assertEqual(z.email, "")
		self.assertEqual(z.password, "")
		self.assertEqual(z.first_name, "")
		self.assertEqual(z.last_name, "")
