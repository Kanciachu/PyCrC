with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    for x in range(0,4):
        print(contents)