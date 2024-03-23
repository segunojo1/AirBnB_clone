#!/usr/bin/python3
"""Base model for airbnb"""
import uuid
import datetime


class BaseModel:
    """base model"""
    def __init__(self):
        """initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str print"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_At time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictt"""
        new_obj = self.__dict__.copy()
        new_obj['__class__'] = self.__class__.__name__
        new_obj['created_at'] = self.created_at.isoformat()
        new_obj['updated_at'] = self.updated_at.isoformat()
        return new_obj
