guests = ['Elon Musk ', 'Stephen Hawking ', 'Neil Tyson ']
wontcoomers = ['Angelina Jolie ', 'Buddha ', 'Tony Stark']

msg = " I would like to invite you to a party with will be held on xyz at xy. Hope you will come - kind regards"



guests.insert( 0, "Alan Turing")
guests.insert(3, "Nikola Tesla ")
guests.append("Edward Snowden ")

guests.sort()

for guest in guests:
    print(f"hello {guest} {msg}")

print(f"{wontcoomers[0]}{wontcoomers[1]}{wontcoomers[2]} won't come")

print(f"{len(guests)} people will come")