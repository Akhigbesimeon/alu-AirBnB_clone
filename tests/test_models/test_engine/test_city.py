import unittest
from city import City


class TestCity(unittest.TestCase):

    def test_city_creation(self):
        # Test creation of an Amenity object
        amenity = City("Free WiFi", "High-speed internet access")
        self.assertEqual(amenity.name, "Free WiFi")
        self.assertEqual(amenity.description, "High-speed internet access")

    def test_display_info(self):
        # Test the display_info method
        city = City("Free WiFi", "High-speed internet access")
        self.assertEqual(city.display_info(), "Amenity: Free WiFi, Description: High-speed internet access")

    def test_update_description(self):
        # Test the update_description method
        city = City("Free WiFi", "High-speed internet access")
        city.update_description("Faster internet connection")
        self.assertEqual(city.description, "Faster internet connection")


if __name__ == '__main__':
    unittest.main()
