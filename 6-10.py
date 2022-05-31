fav_number = {
	'marta': [5],
	'aleks': [10,20],
	'maks': [15,30,45],
	'pawel': [20,40,60,80],
	'antek': [25,50,75,100,125],
}

for name in fav_number.keys():
	print(f"\n{name.title()}")
	for number in fav_number[name]:
		print(f"\t{number}")