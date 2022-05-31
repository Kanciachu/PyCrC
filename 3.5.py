guests = ['Elon Musk ', 'Stephen Hawking ', 'Neil Tyson ', 'Angelina Jolie ', 'Buddha ', 'Tony Stark']
wontcoomers = ['Angelina Jolie ', 'Buddha ', 'Tony Stark']

msg = " I would like to invite you to a party with will be held on xyz at xy. Hope you will come - kind regards"

del guests[3]
del guests[3]
del guests[3]

guests.append("Alan Turing ")
guests.append("Nikola Tesla ")
guests.append("Edward Snowden ")

for guest in guests:
    print(f"hello {guest} {msg}")

print(f"{wontcoomers[0]}{wontcoomers[1]}{wontcoomers[2]} won't come")