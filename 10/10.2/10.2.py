with open("learning_python.txt") as file_object:
    data = file_object.read()
    print(data.replace("python","C"))