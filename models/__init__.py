#!/usr/bin/python3

"""initialization of the modellll which is meant for the file storage stuff"""
from libs import get_classes, classes
from .engine.file_storage import FileStorage

# __all__ = ("classes", "storage")

storage = FileStorage()
# get_classes()
storage.reload()