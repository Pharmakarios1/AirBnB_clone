#!/usr/bin/python3
"""
Test case for review
"""

from models.review import Review
from models import storage
from datetime import datetime
import os
import unittest
from models.engine.file_storage import FileStorage

class TestReview(unittest.TestCase):
	"""class for review model"""

	def test_attributes(self):
		review = Review()
		self.assertIsInstance(review.place_id, str)
		self.assertEqual(review.place_id, "")
		self.assertIsInstance(review.user_id, str)
		self.assertEqual(review.user_id, "")
		self.assertIsInstance(review.text, str)
		self.assertEqual(review.text, "")

	def test_inheritance(self):
		review = Review()
		self.assertIsInstance(review, BaseModel)

