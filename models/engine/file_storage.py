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
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """
        save: serializes __objects to the JSON file (path: __file_path)
        """
        objects = {}
        for key, obj in self.__objects.items():
            objects[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objects, f)

    def reload(self):
        """
        reload deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if not path.exists(self.__file_path):
            return
        with open(self.__file_path) as js:
            des = json.loads(js.read())
            self.__objects = {
                key: classes[key.split(".")[0]](**value)
                for key, value in des.items()
            }
