#task7-4
while True:
    pizza_topping = input("Please enter pizza topping or 'quit' to exit: ")
    if pizza_topping.lower() == 'quit':
        break
    else:
        print(f"You have added '{pizza_topping}' topping.")

#task7-5
print("\n")
while True:
    age = int(input("Enter age for ticket price: "))
    if age <=3:
        print("Ticket is free.")
    elif age < 12:
        print("Ticket is 10$")
    else:
        print("Ticket is 15$")