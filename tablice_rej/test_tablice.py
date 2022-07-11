import unittest
from tablice_rejestracyjne import PlatesGenerator


class TestTablice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.plates = PlatesGenerator().generate_plates()
        cls.list = PlatesGenerator().get_list()

    def test_tablice_total(self):
        self.assertEqual(len(self.plates), 7)

    def test_tablice_letters(self):
        letters = sum(l.isalpha() for l in self.plates)
        self.assertEqual(letters, 3)


    def test_tablice_numbers(self):
        numbers = sum(n.isdigit() for n in self.plates)
        self.assertEqual(numbers, 4)


    def test_tablice_differences(self):
        last = self.list[0]
        actual = self.plates
        self.assertNotEqual(last, actual)