#task9-1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

restaurant = Restaurant("armani", "fine dine")
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

#task9-2
print("\n")

restaurant_2 = Restaurant("big pound", "continental")
restaurant_3 = Restaurant("the place", "chinese")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

#task9-3
print("\n")

class User:
    def __init__(self, fname, lname, age, location):
        self.fname = fname
        self.lname = fname
        self.age = age
        self.location = location
        
    def describe_user(self):
        print(f"{self.fname.title()} {self.lname} is {self.age} old and from {self.location}")

    def greet_user(self):
        print(f"Welcome {self.fname.title()} {self.lname}!")

user = User("David","boom", 45, "australia")
user.describe_user()
user.greet_user()