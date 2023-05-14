#!/usr/bin/python3
"""
This is the base_model test cases
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    
	def test_init_no_args(self):
		bm = BaseModel()
		self.assertIsInstance(bm, BaseModel)
		self.assertIsInstance(bm.created_at, datetime)
		self.assertIsInstance(bm.updated_at, datetime)
		self.assertIsInstance(bm.id, str)
        
	def test_init_with_kwargs(self):
		my_uuid = "00000000-0000-0000-0000-000000000000"
		my_created_at = "2022-01-01T00:00:00.000000"
		my_updated_at = "2022-01-01T00:00:00.000000"
		bm = BaseModel(id=my_uuid, created_at=my_created_at, updated_at=my_updated_at)
		self.assertIsInstance(bm, BaseModel)
		self.assertIsInstance(bm.created_at, datetime)
		self.assertIsInstance(bm.updated_at, datetime)
		self.assertEqual(bm.id, my_uuid)
		self.assertEqual(str(bm.created_at), my_created_at)
		self.assertEqual(str(bm.updated_at), my_updated_at)
        
	def test_save(self):
		bm = BaseModel()
		updated_at_before_save = bm.updated_at
		bm.save()
		self.assertNotEqual(bm.updated_at, updated_at_before_save)
        
	def test_to_dict(self):
		my_uuid = "00000000-0000-0000-0000-000000000000"
		my_created_at = datetime(2022, 1, 1, 0, 0, 0)
		my_updated_at = datetime(2022, 1, 1, 0, 0, 0)
		bm = BaseModel(id=my_uuid, created_at=my_created_at, updated_at=my_updated_at)
		bm_dict = bm.to_dict()
		self.assertIsInstance(bm_dict, dict)
		self.assertEqual(bm_dict['__class__'], 'BaseModel')
		self.assertEqual(bm_dict['id'], my_uuid)
		self.assertEqual(bm_dict['created_at'], '2022-01-01T00:00:00')
		self.assertEqual(bm_dict['updated_at'], '2022-01-01T00:00:00')
        
	def test_str(self):
		my_uuid = "00000000-0000-0000-0000-000000000000"
		my_created_at = datetime(2022, 1, 1, 0, 0, 0)
		my_updated_at = datetime(2022, 1, 1, 0, 0, 0)
		bm = BaseModel(id=my_uuid, created_at=my_created_at, updated_at=my_updated_at)\
		expected_output = "[BaseModel] ({}) {}".format(my_uuid, bm.to_dict())
		self.assertEqual(str(bm), expected_output)



