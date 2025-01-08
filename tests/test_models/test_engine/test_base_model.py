#!/usr/bin/python3
""" 
unittests for BaseModel class
"""
import os
import sys
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """Test BaseModel class"""

    def test_init(self):
        """Test init method"""
        # create and object instance of BaseModel class
        obj = BaseModel()
        # check if obj is instance of BaseModel
        self.assertIsInstance(obj, BaseModel)
        # check if dict contains all expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        # check if P.I attributes are of correct types
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        # create dict to set obj values to with **kwargs
        new_dict = {}
        new_dict["id"] = "012345"
        new_dict["created_at"] = "2023-09-11T16:33:48.491780"
        new_dict["updated_at"] = "2023-09-11T16:35:08.916060"
        # created object instance with **kwargs and run testing
        obj2 = BaseModel(**new_dict)
        self.assertIsInstance(obj2, BaseModel)
        self.assertIn("id", obj2.__dict__)
        self.assertIn("created_at", obj2.__dict__)
        self.assertIn("updated_at", obj2.__dict__)
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)
        #  can also test exact values, including formatting of datetimes
        self.assertEqual(obj2.id, "012345")
        string1 = "2023-09-11 16:33:48.491780"
        self.assertEqual('{}'.format(obj2.created_at), string1)
        string2 = "2023-09-11 16:35:08.916060"
        self.assertEqual('{}'.format(obj2.updated_at), string2)

    def test_str(self):
        """test __str__  method"""
        obj = BaseModel()
        cls = type(obj).__name__
        string = '[{}] ({}) {}'.format(cls, obj.id, obj.__dict__)
        # check if __st__ returns the right representation
        self.assertEqual(obj.__str__(), string)

    def test_save(self):
        """tests save method"""
        obj = BaseModel()
        # test that update_at changes value
        a = obj.updated_at
        obj.save()
        b = obj.updated_at
        self.assertNotEqual(a, b)

    def test_to_dict(self):
        """ Tests to_dict method """
        obj = BaseModel()
        dict_rep = obj.to_dict()
        # check if all keys from obj.__dict__ and __class__ in dict_rep
        for key in obj.__dict__:
            self.assertIn("{}".format(key), dict_rep)
        self.assertIn("__class__", dict_rep)
        # check if dictionary values are correct type
        self.assertIsInstance(dict_rep["id"], str)
        self.assertIsInstance(dict_rep["created_at"], str)
        self.assertIsInstance(dict_rep["updated_at"], str)
        self.assertIsInstance(dict_rep["__class__"], str)
        # check if dictionary values are correct
        self.assertEqual(dict_rep["id"], obj.id)
        self.assertEqual(dict_rep["__class__"], type(obj).__name__)
        string = str(datetime.isoformat(obj.created_at))
        self.assertEqual(dict_rep["created_at"], string)
        string = str(datetime.isoformat(obj.updated_at))
        self.assertEqual(dict_rep["updated_at"], string)
        # check if new instance can be created with to_dict as kwargs
        obj2 = BaseModel(**dict_rep)
        # check if created new instance and set all attributes
        self.assertIsInstance(obj2, BaseModel)
        self.assertIn("id", obj2.__dict__)
        self.assertIn("created_at", obj2.__dict__)
        self.assertIn("updated_at", obj2.__dict__)
        # check if attributes correct type and same value as original
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)
        self.assertEqual(obj2.id, obj.id)
        self.assertEqual(obj2.created_at, obj.created_at)
        self.assertEqual(obj2.updated_at, obj.updated_at)
        self.assertEqual(type(obj2).__name__, type(obj).__name__)
        # check that new object is a different instance
        self.assertIsNot(obj, obj2)