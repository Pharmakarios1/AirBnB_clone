#!/usr/bin/python3
"""
Taste case for state BaseModel
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State

class TestState(unittest.TestCase):
	"""class of state base model"""

def test_name_attribute(self):
	state = State()
	self.assertEqual(state.name, "")
	state.name = "Osogbo"
	self.assertEqual(state.name, "Osogbo")

