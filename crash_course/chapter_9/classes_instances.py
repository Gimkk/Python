#task9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_served):
        self.number_served += increment_served
    
    def show_number_served(self):
        print(f"Number of serverd so far: {self.number_served}")
    
restaurant_1 = Restaurant("Yum", "chinese")
restaurant_1.show_number_served()

restaurant_1.set_number_served(10)
restaurant_1.show_number_served()

restaurant_1.increment_number_served(35)
restaurant_1.show_number_served()

#task9-5
print("\n")

class User:
    def __init__(self, fname, lname, age, location):
        self.fname = fname
        self.lname = fname
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


user = User("David","boom", 45, "australia")
user.describe_user()
user.greet_user()

user.show_logins()
for _counter in range(1,5):
    user.increment_login_attempts()
user.show_logins("increment")
user.reset_login_attempts()
user.show_logins("reset")