#!/usr/bin/python
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        """Set up method that will run before every Test"""
        pass

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        """
        Test if an instance of BaseModel is created correctly.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(instance_dict["created_at"], instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"], instance.updated_at.isoformat())

    def test_save_method(self):
        """
        Test if the save method updates `updated_at` and interacts with FileStorage.
        """
        instance = BaseModel()
        previous_updated_at = instance.updated_at

        with patch('models.base_model.FileStorage') as MockFileStorage:
            mock_storage_instance = MockFileStorage.return_value
            instance.save()

            # Check if `updated_at` is updated
            self.assertNotEqual(instance.updated_at, previous_updated_at)
            self.assertTrue(instance.updated_at > previous_updated_at)

            # Check if FileStorage.new and FileStorage.save are called
            mock_storage_instance.new.assert_called_with(instance)
            mock_storage_instance.save.assert_called()

    def test_str_representation(self):
        """
        Test the __str__ method of BaseModel.
        """
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

if __name__ == "__main__":
    unittest.main()