#1/usr/bin/python3
"""contains a file storage model for storing classes"""
import json
from os import path


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """all returns the dictionary (object)"""
        return self.__objects

    def new(self, obj):
        """
        new sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.obj[key] = obj

    def save(self):
        """
        save: serializes __objects to the JSON file (path: __file_path)
        """
        objects = {}
        for key, obj in self.__objects.items():
            objects[key] = obj.to_dict()

        with open(self.__file_path, mode="w") as f:
            json.dump(objects, f)

    def reload(self):
        """
        reload deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**value)
