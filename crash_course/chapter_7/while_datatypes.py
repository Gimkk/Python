#task7-8
sandwich_order = ["chicken", "club", "egg", "cheese", "vegi"]
finished_sandwich = []

while sandwich_order:
    preparing = sandwich_order.pop()
    print(f"Preparing {preparing} sandwich.")
    finished_sandwich.append(preparing)
print("sandwiches are ready:")
for sandwich in finished_sandwich:
    print(f"\t{sandwich} sandwich")

#task7-9
print("\n")

sandwich_orders = ["pastrami", "chicken", "club", "pastrami", "egg", "cheese", "pastrami", "vegi"]
finished_sandwichs = []

print("Deli is out of pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    preparing = sandwich_orders.pop()
    print(f"Preparing {preparing} sandwich.")
    finished_sandwichs.append(preparing)
print("sandwiches are ready:")
for sandwich in finished_sandwichs:
    print(f"\t{sandwich} sandwich")


#task7-10
print("\n")

poll = {}
message = "if you could visit one place in the world," 
message += "\nwhere would you go?"

while True:
    print(message)
    name = input("Enter your name?: ")
    place = input("Where do you want to go?: ")
    poll[name] = place
    response = input("whould you like to enter another response (yes/no)?: ")
    if response.lower() == "no":
        break

print("---Poll Result---")

for name, place in poll.items():
    print(f"{name.title()} wants to go {place.title()}")