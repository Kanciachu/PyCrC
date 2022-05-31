print("How many peoples are in your diner group?")

people = int(input())

if people > 8:
    print("You will have to wait for your table")
elif people < 0:
    print("you have negative number of friends?")
else:
    print("your table is ready!")