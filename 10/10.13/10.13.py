import json
filepath = "username.json"


def get_username():
    try:
        with open(filepath, "r") as file:
            username = json.load(file)
            return username
    except FileNotFoundError:
        return None


def add_user():
    try:
        with open(filepath, "w") as file:
            username = input("type in your username")
            json.dump(username, file)
            print(f"OK i will remember you {username}")
    except FileNotFoundError:
        return None


def greet_user():
    username = get_username()
    if username:
        if input(f"are you {username}[y] or [n]").upper() == "Y":
            print(f"greethings {username}")
        else:
            add_user()
    else:
        add_user()


greet_user()
