import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class."""

    def setUp(self):
        """Set up resources for testing."""
        self.storage = FileStorage()
        self.test_file = "file.json"

        # Clean up the test environment
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all(self):
        """Test the all() method."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new() method."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test the save() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Check if the file was created
        self.assertTrue(os.path.exists(self.test_file))

        # Check if the data was serialized correctly
        with open(self.test_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, data)

    def test_reload(self):
        """Test the reload() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Clear __objects and reload from file
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

    def test_no_file_reload(self):
        """Test reload() when no file exists."""
        # Ensure no file exists
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        try:
            self.storage.reload()  # Should not raise an exception
        except Exception as e:
            self.fail(f"reload() raised an exception: {e}")

    def test_private_attributes(self):
        """Test private attributes __file_path and __objects."""
        self.assertFalse(hasattr(self.storage, "__file_path"))
        self.assertFalse(hasattr(self.storage, "__objects"))


if __name__ == "__main__":
    unittest.main()
