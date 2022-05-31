import json

number = input("type in your favorite number")

with open("Numbar.json", "w") as plik:
    json.dump(number, plik)
