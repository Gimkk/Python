class User:
    def __init__(self, fname, lname, age, location):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.location = location
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.fname.title()} {self.lname} is {self.age} old and from {self.location}")

    def greet_user(self):
        print(f"Welcome {self.fname.title()} {self.lname}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def show_logins(self, check=None):
        if check:
            print(f"Current login count after {check}: {self.login_attempts}")
        else:
            print(f"Current login count: {self.login_attempts}")