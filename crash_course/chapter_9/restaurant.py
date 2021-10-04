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
