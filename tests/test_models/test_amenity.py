#!/usr/bin/python3
""" amenity class unit tests """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """test the Amenity class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ The name should be a string """
        new = self.value()
        self.assertEqual(type(new.name), str)
