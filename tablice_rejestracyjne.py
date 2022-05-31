import numbers
import random
from itertools import product
from string import ascii_lowercase


class PlatesGenerator:
    def __init__(self, tablice_rejestracyjne):
        self.tablice_rejestracyjne = tablice_rejestracyjne
    def generate_plates(self):
        tablice_rejestracyjne = []
        litery = [''.join(i) for i in product(ascii_lowercase, repeat=3)]
        cyfry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        tablica = random.choice(litery) + str(random.choice(cyfry)) + str(random.choice(cyfry)) + \
                  str(random.choice(cyfry)) + str(random.choice(cyfry))
        while True:
            if tablica in tablice_rejestracyjne:
                continue
            else:
                tablice_rejestracyjne.append(tablica)
                print(tablice_rejestracyjne)
                return tablica

#while True:
pg = PlatesGenerator(tabice_rejestracyjne)
print(pg.generate_plates())

