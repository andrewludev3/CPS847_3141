import unittest
from sample_code import cps3141

class TestCps3141(unittest.TestCase):
    def test_y_equals_7(self):
        self.assertEqual(cps3141(7), 35)

if __name__ == '__main__':
    unittest.main()
