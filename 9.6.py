class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"This restaurant is called : {self.name}, and it serves food from {self.cuisine} cuisine")

    def open(self):
        print(f"The {self.name} is open!")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        self.flavors = flavors
        super().__init__(name, cuisine)

    def display_flavors(self):
        print("YOU CAN BUY HERE ICE CREMES IN FLAVORS AS:")
        for flavor in self.flavors:
            print(flavor)


i = IceCreamStand("frozen", "ice creams", ["vanilia", "chocolate"])

i.describe()
i.open()
i.display_flavors()