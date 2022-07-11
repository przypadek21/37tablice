import random
from itertools import product
from string import ascii_lowercase


class PlatesGenerator:
    def __init__(self):
        self.tablice_rejestracyjne = []

    def generate_plates(self):
        while True:
            litery = [''.join(i) for i in product(ascii_lowercase, repeat=3)]
            cyfry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            tablica = random.choice(litery) + str(random.choice(cyfry)) + str(random.choice(cyfry)) + \
                  str(random.choice(cyfry)) + str(random.choice(cyfry))

            if tablica not in self.tablice_rejestracyjne:
                self.tablice_rejestracyjne.append(tablica)
                return tablica

    def get_list(self):
        return self.tablice_rejestracyjne

pg = PlatesGenerator()
print(pg.get_list())
