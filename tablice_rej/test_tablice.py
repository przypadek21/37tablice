import unittest
from tablice_rejestracyjne import PlatesGenerator

platesToGenerate = 10

class TestTablice(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.pg = PlatesGenerator()
        for _ in range(0, platesToGenerate):
            self.pg.generate_plates()

    def test_get_plates(self):
        self.assertEqual(self.pg.tablice_rejestracyjne, self.pg.get_list())

    def test_tablice_total(self):
        self.assertEqual(len(self.pg.tablice_rejestracyjne), platesToGenerate)

    def test_tablice_letters(self):
        for plate in self.pg.tablice_rejestracyjne:
            letters = sum(l.isalpha() for l in plate)
            self.assertEqual(letters, 3)

    def test_tablice_numbers(self):
        for plate in self.pg.tablice_rejestracyjne:
            numbers = sum(n.isdigit() for n in plate)
            self.assertEqual(numbers, 4)

    def test_tablice_differences(self):
        alreadyExists = {}
        for plate in self.pg.tablice_rejestracyjne:
            self.assertTrue(plate not in alreadyExists)
            alreadyExists[plate] = True
if __name__ == '__main__':
    unittest.main()
