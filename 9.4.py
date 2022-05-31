class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        print(f"This restaurant is called : {self.name}, and it serves food from {self.cuisine} cuisine")

    def open(self):
        print(f"The {self.name} is open!")

    def set_numbers_served(self, number):
        self.number_served = number

    def increase_serv(self):
        self.number_served += 1


rest = Restaurant("aaa", "aaa")
print(rest.number_served)
rest.set_numbers_served(10)
print(rest.number_served)
rest.increase_serv()
print(rest.number_served)