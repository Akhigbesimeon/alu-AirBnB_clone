""" This module contains the test cases for the FileStorage class. """

import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstantiation(unittest.TestCase):
    """
    Test class for testing the instantiation of the FileStorage class.
    """

    def test_file_storage_instantiation_no_args(self):
        """
        Test that FileStorage can be instantiated with no arguments
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_torage_with_args(self):
        """
        Test that FileStorage cannot be instantiated with arguments
        """
        self.assertRaises(TypeError, FileStorage, None)

    def test_storage_initializes(self):
        """ Test that the storage variable in the models module is an instance
        of the FileStorage class.
        """

        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    """
    Test class for testing the FileStorage class.
    """

    def setUp(self):
        """
        Set up a test environment with a temporary file for testing file storage
        """
        self.test_file = "test_file.json"

    def tearDown(self):
        """
        Clean up the test environment by removing the temporary file
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        """
        Test if the all() method returns a dictionary.
        """
        self.assertEqual({}, models.storage.all())

    def test_new(self):
        """
        Test that the new() method adds a new object to the storage dictionary.
        """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", models.storage.all())

    def test_new_with_args(self):
        """Test that the new() method raises TypeError when given additional
        arguments."""       
        self.assertRaises(TypeError, models.storage.new, 1)

    def test_new_with_none(self):
        """
        Test that creating a new object with None raises AttributeError. This
        ensures that the new() method does not allow None as an argument.
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """
        Test that the save() method saves objects to a file and then reloads
        them back into the storage dictionary when the reload() method is
        called.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded objects match the original objects
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save_to_file(self):
        """
        Test saving objects to a file and check if the file is created.
        """
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """
        Test that the reload() method raises TypeError when the file is empty or does not exist
        """
        with self.assertRaises(TypeError):
            models.storage.reload()

if __name__ == "__main__":
    unittest.main()