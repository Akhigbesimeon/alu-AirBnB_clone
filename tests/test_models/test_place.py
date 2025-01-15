#!/usr/bin/python3
""" Place module """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ test the Place class """ 

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ the city id should be a string """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ the user id should be a string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ The name should be a string """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """  The description should be a string """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ 
        Tests that the number of rooms in a Place is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Tests that the number of bathrooms in a Place is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Tests that the maximum number of guests in a Place is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Tests that the price by night in a Place is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Tests that the latitude of a Place is a float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Tests that the longitude of a Place is a float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Tests that the amenity_ids of a Place is a list.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)