class User:

    def __init__(self, first_name, last_name, nick, account_type):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.nick = nick.capitalize()
        self.account_type = account_type.capitalize()

    def describe_user(self):
        print(f"first name of the user is : {self.first_name}\n"
              f"last name of the user is : {self.last_name}\n"
              f"nick of the user is : {self.nick}\n"
              f"User account type is : {self.account_type}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")


user1 = User("adam", "nowak","adamek","pro")
user1.describe_user()
user1.greet_user()