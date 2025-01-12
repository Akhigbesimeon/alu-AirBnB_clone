import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class that defines all common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs is not empty, recreate an instance from dictionary representation.
        Otherwise, create a new instance with unique ID and current datetime.
        """
        if kwargs:  # Recreate an instance from a dictionary
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert string to datetime
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:  # Create a new instance
            self.id = str(uuid.uuid4())  # Assign unique ID
            self.created_at = datetime.now()  # Current datetime for creation
            self.updated_at = datetime.now()  # Current datetime for updates

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        # Create an instance of FileStorage and call save
        storage = FileStorage()
        storage.save()
  
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
