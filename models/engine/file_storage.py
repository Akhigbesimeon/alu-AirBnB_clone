import json
from models.base_model import BaseModel

class FileStorage:
    """
    Handles storage and retrieval of objects to/from a JSON file.
    """

    __file_path = "file.json"  # File to store objects
    __objects = {}  # Dictionary to store objects

    def all(self):
        """
        Returns a dictionary of all objects in storage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes all objects in storage to a JSON file.
        Ensures that only JSON serializable data is saved.
        """
        with open(FileStorage.__file_path, 'w') as f:
            # Convert all objects to dictionaries (using the to_dict method)
            dict_representation = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            # Save the serialized dictionary to the JSON file
            json.dump(dict_representation, f)

    def reload(self):
    """
    Deserializes objects from the JSON file to storage
    """
    try:
        with open(FileStorage.__file_path, 'r') as f:
            dict_representation = json.load(f)
            for key, value in dict_representation.items():
                class_name = value["__class__"]
                class_obj = globals()[class_name]  # Get the class by name
                self.new(class_obj(**value))
    except FileNotFoundError:
        pass  # If file does not exist, we just skip loading
    except json.JSONDecodeError:
        print("Warning: file.json is empty or corrupted, starting with an empty storage.")
        # Optionally create an empty file or handle this scenario
        pass
