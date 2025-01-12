import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
      pass

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())  # Assign unique id
        self.created_at = datetime.now()  # Current datetime for creation
        self.updated_at = datetime.now()  # Current datetime for updates

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        # Create a copy of __dict__ to ensure original data isn't modified
        dict_representation = self.__dict__.copy()
        
        # Add class name to the dictionary
        dict_representation["__class__"] = self.__class__.__name__

        # Convert `created_at` and `updated_at` to ISO format strings
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()

        return dict_representation