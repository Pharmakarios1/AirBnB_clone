#!/usr/bin/python3
"""
This is a special function that is called when a package is executed
In this case, in other to create a unique FileStorage instance for this application,
file_storage.py is imported which is equal to storage and reload is called. 
"""

from models.engin.file_storage import FileStorage
storage = FileStorage
storage.reload()
