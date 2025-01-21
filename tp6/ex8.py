import unittest
from ex1 import safe_division

class test(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10,0)

if __name__=="__main__":
    unittest.main()