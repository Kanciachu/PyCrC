class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"This restaurant is called : {self.name}, and it serves food from {self.cuisine} cuisine")

    def open(self):
        print(f"The {self.name} is open!")


rest1 = Restaurant("drewnem palone", "pizza")
rest2 = Restaurant("hulaj dusza", "cassual")
rest3 = Restaurant("ramenownia", "azjatycka")

restauracje = [rest1, rest2, rest3]

for restauracja in restauracje:
    restauracja.describe()
    restauracja.open()