#!usr/bin/python
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity."""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize an Amenity instance by inheriting from BaseModel.
        Accepts variable arguments and keyword arguments.
        """

        super().__init__(*args, **kwargs)