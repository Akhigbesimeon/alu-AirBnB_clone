"""Defines a class for serializing and deserializing JSON files."""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        Args:
            obj: The object to be added to __objects.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(
                {key: value.to_dict() for key, value in self.__objects.items()},
                file
            )

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        Does nothing if the file does not exist.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    self.__objects[key] = BaseModel(**value)
