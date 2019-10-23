import unittest
from MyMath import MyMath

class testSum(unittest.TestCase):
    def test(self):
        self.assertEqual(MyMath.sum(2, 3), 5)

class testSubstract(unittest.TestCase):
    def test(self):
        self.assertEqual(MyMath.substract(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
