favorite_places = {
	'antek': ['zakopane', 'chorwacja', 'las'],
	'hubert': ['morze' , 'gory' , 'kalisz'],
	'kinga': ['egipt' , 'grecja' , 'chorwacja'],
}			



for name in favorite_places.keys():
	print(f"\n{name}")
	for places in favorite_places[name]:
		print(f"\t{places.title()}")
