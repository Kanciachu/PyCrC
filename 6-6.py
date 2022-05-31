favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

peoples = ['adam', 'jen','antek','phil']

for people in peoples:
	if people not in favorite_languages:
		print(f"{people.title()} please take a poll :C")
	else:
		print(f"thank you for taking the poll {people.title()} C:")	