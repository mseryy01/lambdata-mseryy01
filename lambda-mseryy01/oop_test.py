import unittest
from oop import show_age, show_name

class AgeTest(unittest.TestCase):
    """Obligatory docstring, test show_age and show_name functions!"""
    def test_age32(self):
        self.assertEqual(show_age(32), 33)

    def test_name(self):
        self.assertEqual(show_name('Mike'),'Mike')

if __name__ == '__main__':
    unittest.main()
