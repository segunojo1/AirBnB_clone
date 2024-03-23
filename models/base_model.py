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
