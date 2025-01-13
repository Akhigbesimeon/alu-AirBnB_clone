import uuid
from datetime import datetime

class BaseModel:
   
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs is not empty, recreate an instance from dictionary representation.
        Otherwise, create a new instance with unique ID and current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()  # Update the `updated_at` field
        # Lazy import to avoid circular import
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.new(self)  # Add the instance to storage
        storage.save()  # Save to the file

    def to_dict(self):
        """
        Returns a dictionary representation of the instance that is JSON serializable.
        """
        dict_representation = self.__dict__.copy()  # Copy the instance's dictionary

        # Convert datetime attributes to ISO format strings
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()

        # Add class name to the dictionary for identification
        dict_representation["__class__"] = self.__class__.__name__

        # Ensure all values in the dictionary are JSON serializable
        for key, value in dict_representation.items():
            if isinstance(value, datetime):
                dict_representation[key] = value.isoformat()

        return dict_representation
