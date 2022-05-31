country_rivers = {'poland': "wisla" , 'egipt': "nile" , 'france': "loara" }

for country , river in country_rivers.items():
	print(f"{river.title()} is the longest river of {country.title()}")

for river in country_rivers.values():
	print(f"{river}")

for country in country_rivers.keys():
	print(f"{country}")