cities = {
	'warszawa':{'population': 1776000,'country':'Poland','fact':'Warsaw’s Lazienki Park is one of the largest palace and park ensembles in Europe, and hosts free Sunday concerts from May to October.'},
	'paris':{'population':2148271,'country':'France','fact':'The oldest house in Paris is located at 51, rue de Montmorency, 3. Arrondissement. It was built in 1407!'},
	'london':{'population':8908081,'country':'England','fact':'London Has 170 Museums'},
}

for city in cities.keys():
	print(f"\n{city.title()}")
	for info , data in cities[city].items():
		print(f"\t{info.title()}: {data}")