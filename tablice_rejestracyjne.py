import random
from itertools import product
from string import ascii_lowercase


class PlatesGenerator:
    def generate_plates(self):
        tablice_rejestracyjne = []
        litery = [''.join(i) for i in product(ascii_lowercase, repeat=3)]
        cyfry = [random.randrange(0, 10 ** 4)]
        tablica = random.choice(litery) + str(random.choice(cyfry))
        tablice_rejestracyjne.append(tablica)

        return tablica

while True:
        pg = PlatesGenerator()
        print(pg.generate_plates())

