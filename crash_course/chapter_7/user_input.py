#task7-1
car = input("What kind of rental car you like: ")
print(f"Let me see if I can find you a {car.title()}.")

#task7-2
print("\n")

people_count = int(input("How many people are in the dinner: "))
if people_count > 8:
    print("Wait for the table.")
else:
    print("table is ready.")

#task7-3
print("\n")

number = int(input("Enter the number: "))
if number%10:
    print(f"{number} is not multiple of 10")
else:
    print(f"{number} is multiple of 10")