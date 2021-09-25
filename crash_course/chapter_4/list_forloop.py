#task4-1
pizzas = ["chicken", "cheese", "vegi", "prawn"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("\nHow much you like pizza?\n")

#task4-2
animals = ["cat", "dog", "lizard", "fish"]

for animal in animals:
    print(f"A {animal} would make a great pet")

print("\nAny of these animals would make a great pet\n")

#task4-3
for number in range(1,21):
    print(number)

#task4-4
million = [number for number in range(1,100)]
print(million)

#task4-5
print(f"Minimum number in list min(million): {min(million)}")
print(f"Maximum number in list max(million): {max(million)}")
print(f"Sum of numbers in list sum(million): {sum(million)}")

#task4-6
for odd in range(1,21,2):
    print(f"odd number in range range(1,21,2): {odd}")

#task4-7
for number in range(3,31,3):
    print(f"Multiples of {number} is: {number*number}")

#task4-8
cubes = [number**3 for number in range(1,11)]
for cube in cubes:
    print(cube)
#task4-9

