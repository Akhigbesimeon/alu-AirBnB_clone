import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        import json
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Reloads the objects from the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
