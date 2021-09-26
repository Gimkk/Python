#task6-4
countries = {"\naus": "australia", "uk": "united kingdom", "sa": "south africa", "nz": "new zeland",}
for key,value in countries.items():
    print(f"{key.title()} is short for: {value.title()}")

#task6-5
print("\n")
rivers = {"nile": "eygpt", "amazon": "brazil", "yangtze": "china", "mekong": "china",}
for key,value in rivers.items():
    print(f"River {key.title()} runs through {value.title()}")

print("\n")
for key in sorted(rivers.keys()):
    print(f"{key.title()} is one of the main river.")

print("\n")
for key in sorted(set(rivers.values())):
    print(f"{key.title()} has one of the main river.")

#task6-6
names = ["eric", "smith", "leo", "mark", "simon","david", "mike", "mark", "geoff"]
languages = {"eric": "python", "smith": "java", "leo": "c",}
languages["david"] = "java"
languages["mike"] = "c++"
languages["mark"] = "python"

print("\n")
for name in names:
    if name not in languages.keys():
        print(f"{name.title()} would you kindly fill the poll!")
    else:
        print(f"Thank you {name.title()} for the poll!")
