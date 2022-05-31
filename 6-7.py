czlowiek_0 = {'first_name': "antek" , 'last_name': "wanot", 'age': 22 ,'city':"kutno" }
czlowiek_1 = {'first_name': "hubert" , 'last_name': "antonczak", 'age': 22 ,'city':"kutno" }
czlowiek_2 = {'first_name': "szymon" , 'last_name': "neugebauer", 'age': 2 ,'city':"kutno" }

ludzie = [czlowiek_0 , czlowiek_1 , czlowiek_2]


for ludz in ludzie:
	print(f"{ludz['first_name'].title()}")
	print(f"\t{ludz['last_name'].title()}")
	print(f"\t{ludz['age']}")
	print(f"\t{ludz['city'].title()}\n")