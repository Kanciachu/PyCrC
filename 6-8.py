animal_0 ={'animal':'cat','name':'kot', 'owner': 'adam'}
animal_1 ={'animal':'dog','name':'lapa', 'owner': 'anthony'}
animal_2 ={'animal':'turtle','name':'turtles', 'owner': 'radek'}
animal_3 ={'animal':'cat','name':'rysiek', 'owner': 'james'}
animal_4 ={'animal':'parrot','name':'jack', 'owner': 'joe'}

pets = [animal_0, animal_1, animal_2, animal_3, animal_4]


for pet in pets:
	print(f"{pet['animal'].title()}")
	print(f"\tpet name: {pet['name'].title()}")
	print(f"\towner name: {pet['owner'].title()}\n")