#!/usr/bin/python3
"""test file for city class"""

import unittest
from models.city import City


class TestUserModel(unittest.TestCase):
    """creating a testcase class that inherits from unittest.TestCase"""

    def setUp(self):
        """setting up the object for testing"""
        self.city_model = City()

    def test_instance(self):
        self.assertIsInstance(self.city_model, City)

    def test_name(self):
        self.assertIsInstance(self.city_model.name, str)
        self.assertEqual(self.city_model.name, "")
        self.city_model.name = "kigali"
        self.assertEqual(self.city_model.name, "kigali")

    def test_state_id(self):
        self.assertIsInstance(self.city_model.state_id, str)
        self.assertEqual(self.city_model.state_id, "")
        self.city_model.state_id = "1234"
        self.assertEqual(self.city_model.state_id, "1234")


if __name__ == "__main__":
    unittest.main()
