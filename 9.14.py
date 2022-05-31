from random import randint

class Dice():

    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return randint(1,self.sides)


dice1 = Dice(10)
dice2 = Dice(20)

for x in range(0,11):
    print(f" dice 1 : {dice1.roll_dice()}")
    print(f" dice 2 : {dice2.roll_dice()}")
