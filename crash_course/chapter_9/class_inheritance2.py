#task9-9

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

class Privileges:
    def __init__(self):
       self.privileges = ["can add post", "can delete post", "can ban user",]

    def show_privileges(self):
        print(f"User has following privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")

class Admin(User):
    def __init__(self, fname, lname, age, location):
        super().__init__(fname, lname, age, location)
        self.privilege = Privileges()
    

user = Admin("David","boom", 45, "australia")
user.describe_user()
user.greet_user()
user.privilege.show_privileges()
user.show_logins()
for _counter in range(1,5):
    user.increment_login_attempts()
user.show_logins("increment")
user.reset_login_attempts()
user.show_logins("reset")

#task9-10
print("\n")

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_fuel_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car has 150l fuel tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size <= 75:
            self.battery_size = 100
            print("Battery is now upgraded to 100-kwh")
        else:
            print(f"Battery is alredy {self.battery_size}-kWh")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()
    
    def fill_fuel_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
