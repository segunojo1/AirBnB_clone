from .base_model import BaseModel
"""the user model created now"""


class User(BaseModel):
    """user class that inherits from the base model"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""