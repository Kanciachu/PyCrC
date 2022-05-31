class User:

    def __init__(self, first_name, last_name, nick, account_type):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.nick = nick.capitalize()
        self.account_type = account_type.capitalize()
        self.login_attempts = 0

    def describe_user(self):
        print(f"first name of the user is : {self.first_name}\n"
              f"last name of the user is : {self.last_name}\n"
              f"nick of the user is : {self.nick}\n"
              f"User account type is : {self.account_type}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

    def increase_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        

us = User("adam", "nowak", "adamek", "pro")
us.increase_login_attempts()
us.increase_login_attempts()
us.increase_login_attempts()
us.increase_login_attempts()
print(us.login_attempts)
us.reset_login_attempts()
print(us.login_attempts)