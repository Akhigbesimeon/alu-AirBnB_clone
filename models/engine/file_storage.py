import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)
    
   def reload(self):
    """Deserializes the JSON file to __objects, if it exists."""
    try:
        with open(self.__file_path, "r") as f:
            obj_dict = json.load(f)
        for key, value in obj_dict.items():
            class_name = value["__class__"]
            self.__objects[key] = globals()[class_name](**value)
    except FileNotFoundError:
        pass

