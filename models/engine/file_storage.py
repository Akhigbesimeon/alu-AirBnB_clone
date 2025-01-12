"""Defines a class for serializing and deserializing JSON files."""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path )"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump({key: value.to_dict() for key, value in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the JSON file exists.
        If the file doesn't exist, does nothing. No exception is raised.
        """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    FileStorage.__objects[key] = BaseModel(**value)
        else:
            pass    