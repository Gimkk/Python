#task8-3

def make_shirt(size, message):
    print(f"Shirt size is '{size}' with '{message}' printed on it")

make_shirt("small", "Hello world!")
make_shirt(message="This is python", size="large")

#task8-4
print("\n")

def make_shirt2(size="large", message="I love python"):
    print(f"Shirt size is '{size}' with '{message}' printed on it")

make_shirt2()
make_shirt2("medium")
make_shirt2(message="Python love")

#task8-5
print("\n")

def describe_city(city, country="australia"):
    print(f"{city.title()} is in {country.title()}")

describe_city("sydney")
describe_city("melbourne")
describe_city("paris", "france")
