import random
from itertools import product
from string import ascii_lowercase


class PlatesGenerator:
    def generate_plates(self):
        tablice_rejestracyjne = []
        litery = [''.join(i) for i in product(ascii_lowercase, repeat=3)]
        cyfry = [random.randrange(0, 10 ** 4)]
        tablica = random.choice(litery) + str(random.choice(cyfry))
        while True:
            if tablica in tablice_rejestracyjne:
                continue
            else:
                tablice_rejestracyjne.append(tablica)

        return random.choice(tablice_rejestracyjne)


pg = PlatesGenerator()
pg.generate_plates()
