import random
from itertools import product
from string import ascii_lowercase

tablice_rejestracyjne = []

while True:
    litery = [''.join(i) for i in product(ascii_lowercase, repeat=3)]
    cyfry = [random.randrange(0,10**4)]
    tablica = random.choice(litery) + str(random.choice(cyfry))
    if tablica in tablice_rejestracyjne:
        continue
    else:
        tablice_rejestracyjne.append(tablica)
        print(random.choice(tablice_rejestracyjne))