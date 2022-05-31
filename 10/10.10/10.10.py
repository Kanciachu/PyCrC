with open("book.txt") as file_object:
    for line in file_object:
        try:
            print(line)
        except UnicodeDecodeError:
            pass
        else:
            print(" ")
