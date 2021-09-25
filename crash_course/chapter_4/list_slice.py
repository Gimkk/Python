#task4-10
foods = ["pizza", "falafel", "burger", "bbq", "cannoli"]

for food in foods[:3]:
    print(f"The first three iteams from the foods list: {food}")

for food in foods[1:4]:
    print(f"The middle three iteams from the foods list: {food}")

for food in foods[-3:]:
    print(f"The last three iteams from the foods list: {food}")

#task4-11
pizza = ["chicken", "cheese", "vegi", "prawn"]

friend_pizza = pizza[:]
pizza.append("nutella")
friend_pizza.append("tikka")

for item in pizza:
    print(f"My favorite pizza: {item}")

for item in friend_pizza:
    print(f"My friends favorite pizza: {item}")

#task4-12
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for my_food in my_foods:
    print(f"My favorite foods are: {my_food}")

for friend_food in friend_foods:
    print(f"\nMy friend's favorite foods are: {friend_food}")


