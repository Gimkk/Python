#task6-7
person_1 = {"first_name":"mark", "last_name":"smith", "age":45, "city":"sydney",}
person_2 = {"first_name":"eric", "last_name":"will", "age":30, "city":"melbourne",}

people = [person_1, person_2]

for person in people:
    for key, value in person.items():
        print(f"Person's {key}: {value}")

#task6-8
print("\n")
animal_1 = {"kind":"cat", "owner":"smith",}
animal_2 = {"kind":"dog", "owner":"will",}

pets = [animal_1, animal_2]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")

#task6-9
print("\n")

fav_places = {
    "mike": ["zoo", "wild life park", "water park"],
    "eric": ["cinema", "bowling"],
    "david": ["zoo", "bowling"]
}

for name, places in fav_places.items():
    print(f"{name.title()}'s fav places:")
    for place in places:
        print(f"\t{place.title()}")

#task6-10
print("\n")
fav_numbers = {"simon":[9, 1, 5, 9], "eric":[7,8,0], "jim":[6],}
fav_numbers["mike"] = [5,9,7,3,0]
fav_numbers["david"] = [2,5]

for name, numbers in fav_numbers.items():
    if len(numbers)==1:
        print(f"{name.title()}'s fav number:")
    else:
        print(f"{name.title()}'s fav numbers:")
    for number in numbers:
        print(f"\t{number}")

#task6-11
print("\n")
cities= {
    "sydney": {"country": "australia", "papulation": "10 milion", "fact": "costal city",},
    "london": {"country": "england", "papulation": "50 milion", "fact": "non-costal city",},
    "new york": {"country": "usa", "papulation": "80 milion", "fact": "costal city",},
    "tokyo": {"country": "japan", "papulation": "100 milion", "fact": "costal city",}
}

for city, details in cities.items():
    print(f"City {city.title()}")
    for key, value in details.items():
        print(f"\t{key}:{value}")

#task6-12
print("\n")
