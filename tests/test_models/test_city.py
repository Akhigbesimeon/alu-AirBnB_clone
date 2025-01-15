#!/usr/bin/python3
""" City module """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test the City class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ the state id should be a string """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ The name should be a string """
        new = self.value()
        self.assertEqual(type(new.name), str)