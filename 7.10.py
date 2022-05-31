response = ""
response_list = []
flag = 1

while flag == 1:
    response = input("what are your dream vacations?")
    if response == "stop":
        break
    response += " NAME: " + input("what is your name?")
    response_list.append(response)

for response in response_list:
    print(response)