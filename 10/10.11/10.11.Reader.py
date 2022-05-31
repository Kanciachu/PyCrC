import json

try:
    with open("numbar.json", "r") as plik:
        number = json.load(plik)
        print(number)
except FileNotFoundError:
    print("nikt nie zapisał liczby")
else:
    print("oto liczba lib jej brak")