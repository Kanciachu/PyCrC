class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"This restaurant is called : {self.name}, and it serves food from {self.cuisine} cuisine")

    def open(self):
        print(f"The {self.name} is open!")


rest1 = Restaurant("jasniepanska", "pizza")
rest1.describe()
rest1.open()