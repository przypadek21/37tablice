import sys
password = []
characters_left = 1

password_length = int(input("Jak długie ma byc haslo?"))


if password_length < 5 or password_length < 0:
    print("Haslo jest za krotkie(min. 5 znakow)")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("Ile małych liter ma miec haslo?"))
if lowercase_letters < 0 or lowercase_letters > characters_left:
    print("Liczba mały liczb nie moze przekraczac wszystkich znaków")
    sys.exit(0)
else:
    characters_left -= lowercase_letters

uppercase_letters = int(input("Ile duzych liter ma miec haslo?"))
if uppercase_letters > characters_left - uppercase_letters:


special_characters = int(input("Ile znaków specjlanych ma miec haslo"))
digits = int(input("Ile znaków spec. ma miec haslo"))
