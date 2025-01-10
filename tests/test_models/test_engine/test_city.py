# Create the test case for city
import unittest
from models.city import multiply
class TestMult(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)  # 2 * 4 = 8
        self.assertEqual(multiply(0, 3), 0)  # 0 * 3 = 0

# Run the tests when the file is executed
if __name__ == "__main__":
    unittest.main()