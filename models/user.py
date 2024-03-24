#!/usr/bin/python3
"""the user model created now"""


class User(BaseModel):
    """user class that inherits from the base model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)