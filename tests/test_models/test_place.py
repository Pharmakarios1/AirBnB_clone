#!/usr/bin/python3
"""Tests for the `city` module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):

	def setUp(self):
		self.place = Place()

	def test_instance(self):
		p = Place()
		self.assertIsInstance(p, Place)

	def test_attributes(self):
		self.assertEqual(self.place.city_id, "")
		self.assertEqual(self.place.user_id, "")
		self.assertEqual(self.place.name, "")
		self.assertEqual(self.place.description, "")
		self.assertEqual(self.place.number_rooms, 0)
		self.assertEqual(self.place.number_bathrooms, 0)
		self.assertEqual(self.place.max_guest, 0)
		self.assertEqual(self.place.price_by_night, 0)
		self.assertEqual(self.place.latitude, 0.0)
		self.assertEqual(self.place.longitude, 0.0)
		self.assertEqual(self.place.amenity_ids, [])

	def test_city_id(self):
		p = Place()
		self.assertIsInstance(p.city_id, str)

	def test_name(self):
		p = Place()
		self.assertIsInstance(p.name, str)

	def test_integer_attributes(self):
		p = Place()
		self.assertIsInstance(p.number_rooms, int)
		self.assertIsInstance(p.number_bathrooms, int)
		self.assertIsInstance(p.max_guest, int)
		self.assertIsInstance(p.price_by_night, int)

	def test_float_attributes(self):
		p = Place()
		self.assertIsInstance(p.latitude, float)
		self.assertIsInstance(p.longitude, float)
