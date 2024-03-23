#!/usr/bin/python3
"""Import modules datetime, uuid4 and storage"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for  models in the system"""

    def __init__(self, *args, **kwargs):
        """new instantiation of a new basemodel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    for ["created_at", "updated_at"] in key:
                        value = datetime.fromisoformat(value)
                        continue
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns a string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_At time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """converts the instance to dictionary"""
        new_obj = self.__dict__.copy()
        new_obj['__class__'] = self.__class__.__name__
        new_obj['created_at'] = self.created_at.isoformat()
        new_obj['updated_at'] = self.updated_at.isoformat()
        return new_obj
