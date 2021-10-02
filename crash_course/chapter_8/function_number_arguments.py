#task8-12

def make_sandwich(*args):
    print("Your sandwich will have:")
    for item in args:
        print(f"\t{item}")

make_sandwich("chicken","mayo","salad")
make_sandwich("tuna","latus")
make_sandwich("turky","bbq", "chili","cheese")

#task8-13
print("\n")

def build_profile(first_name, last_name, **kwargs):
    kwargs["first name"] = first_name
    kwargs["last name"] = last_name
    return kwargs

user_profile = build_profile("Mark", "Smith", location="sydney",age="30")
print(user_profile)

#task8-14
print("\n")

def make_car(make, model, **kwargs):
    kwargs["make"] = make
    kwargs["model"] = model
    return kwargs

car = make_car("Mazda", "Mazda3", color="black", type="autometic")
print(car)