#task6-1
person = {"first_name":"Mark", "last_name":"smith", "age":45, "city":"sydney",}
print(f"First name: {person['first_name'].title()}")
print(f"Last name: {person['last_name'].title()}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

#task6-2
fav_number = {"simon":9, "eric":7, "jim":6,}
fav_number["mike"] = 5
fav_number["david"] = 2

print(f"\nSimon's Fav number: {fav_number['simon']}")
print(f"Eric's Fav number: {fav_number['eric']}")
print(f"Jim's Fav number: {fav_number['jim']}")
print(f"Mike's Fav number: {fav_number['mike']}")
print(f"David's Fav number: {fav_number['david']}")

#task6-3
countries = {"\naus":"australia", "uk":"united kingdom", "sa":"south africa","nz":"new zeland",}
print(f"Aus is short for: {countries.get('aus', 'no country found').title()}")
print(f"UK is short for: {countries.get('uk', 'no country found').title()}")
print(f"SA is short for: {countries.get('sa', 'no country found').title()}")
