# !/usr/bin/python3
"""
Test cases for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Tests that a BaseModel instance is properly initialized with an id,
        created_at and updated_at attributes.
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Tests that the save method of a BaseModel instance updates the
        updated_at attribute.
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        current_updated_at = my_model.updated_at
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.created_at.isoformat())

    def test_str(self):
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.to_dict()), str(my_model))


if __name__ == '_main_':
    unittest.main()