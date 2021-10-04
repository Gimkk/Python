#task9-6
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

class IcreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "cookies N' cream", "Strawberry", "cookie dough"]
    
    def show_flavours(self):
        print("Current available ice cream flavours:")
        for flavour in self.flavors:
            print(f"\t{flavour.title()}")

    
icecream_1 = IcreamStand("Yum", "Ice Cream")
icecream_1.show_flavours()
icecream_1.show_number_served()

icecream_1.set_number_served(10)
icecream_1.show_number_served()

icecream_1.increment_number_served(35)
icecream_1.show_number_served()


#task9-7
print("\n")

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

class Admin(User):
    def __init__(self, fname, lname, age, location):
        super().__init__(fname, lname, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user",]
    
    def show_privileges(self):
        print(f"User has following privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")


user = Admin("David","boom", 45, "australia")
user.describe_user()
user.greet_user()
user.show_privileges()
user.show_logins()
for _counter in range(1,5):
    user.increment_login_attempts()
user.show_logins("increment")
user.reset_login_attempts()
user.show_logins("reset")