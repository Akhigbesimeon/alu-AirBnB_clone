"""docstring for the whole module"""

from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now() 
    def __str__(self):
        return f"[{self.__class__}] ({self.id}) {self.__dict__}"
    def save(self):
        self.updated_at = datetime.now()  
    def to_dict(self):
        iso_time = "%Y-%m-%d %H:%M:%S.%f"
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.strftime(iso_time)
        rdict["updated_at"] = self.updated_at.strftime(iso_time)
        rdict["__class__"] = self.__class__.__name__
        return rdict
