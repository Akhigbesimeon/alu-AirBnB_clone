#!/usr/bin/python
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state."""
    name = ""

def __init__(self, *args, **kwargs):
        """initialise class"""
        super().__init__(*args, **kwargs)