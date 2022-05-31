name = input("Whats you're name")
times = 0
with open("guest_book.txt", "a") as file_object:
    while name != "exit":
        print(f"hello {name} !")
        file_object.write(f"{name} was there {times} times\n")
        times += times + 1
        name = input("Whats you're name")