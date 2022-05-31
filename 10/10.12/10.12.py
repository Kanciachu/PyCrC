import json

try:
    with open("numbar.json", "r") as plik:
        number = json.load(plik)
except FileNotFoundError:
    number = input("type in your favorite number")
    with open("Numbar.json", "w") as plik:
        json.dump(number, plik)
else:
    print(number)
    print("oto liczba lub jej brak")

