name = input("Whats you're name")

with open("guest.txt", "a") as file_object:
    file_object.write(f"{name}\n")

