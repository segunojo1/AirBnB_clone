#!/usr/bin/python3
"""the user model created now"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class that inherits from the base model"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""