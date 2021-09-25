names = ["eric", "smith", "leo", "mark","simon"]
greeting = f"Hello {names[0].title()}!"
print(greeting)
greeting = f"Hello {names[-1].title()}!"
print(greeting)
motorbikes = ["Honda", "Yamaha", "Suzuki"]
print(f"\nList: {motorbikes}")
print(f"List motorbikes[0]: {motorbikes[0]}")
motorbikes[0] = "Ducati"
print(f"List motorbikes[0]='Ducati': {motorbikes}")
motorbikes.append("Honda")
print(f"List motorbikes.append('Honda'): {motorbikes}")
motorbikes.insert(1,"BMW")
print(f"List motorbikes.insert(1,'BMW'): {motorbikes}")
del motorbikes[1]       # del will remove the value without using it
print(f"List del motorbikes[1]: {motorbikes}")
print(f"List motorbikes.pop(): {motorbikes.pop()}")     #pop() will delete the value but allow the use of it
print(f"List motorbikes after pop(): {motorbikes}")
popped_motorbikes = motorbikes.pop()
print(f"List motorbikes after another popped_motorbikes = motorbikes.pop(): {motorbikes}")
print(f"Popped_motorbikes : {popped_motorbikes}")
print(f"List motorbikes.pop(0): {motorbikes.pop(0)}")
print(f"List: {motorbikes}")

fruits = ["banana", "orange", "apple", "peach"]
print(f"\nList fruits: {fruits}")
fruits.remove('orange')     #remove() only delete the first occurrence, more then 1 same value use loop
print(f"List fruits.remove('orange'): {fruits}")
expensive = "apple"
fruits.remove(expensive)
print(f"expensive = '{expensive}', List fruits.remove('expensive'): {fruits}")

#task 34
guests = ["David", "Mike", "Geoff"]
print(f"\nList guests: {guests}")
print(f"guest '{guests[1]}' can't make it")
guests[1] = "Tom"
print(f"updated guests: {guests}")
guests.insert(0,"Glen")
guests.insert(2,"Gareth")
guests.append("William")
print(f"final guests: {guests}")
print("Sorry only invite 2 guests")
print(f"sorry {guests.pop()}!")
print(f"sorry {guests.pop()}!")
print(f"sorry {guests.pop()}!")
print(f"sorry {guests.pop()}!")
print(f"Only guests: {guests}")
del guests[1]
del guests[0]
print(f"no guests: {guests}")

#task 3.5
places = ["sydney", "london", "tokyo", "paris"]

print(f"\nlist Places orignal: {places}")
print(f"list sorted(Places): {sorted(places)}")
print(f"list after sorted(Places): {places}")
places.reverse()
print(f"list after places.reverse(): {places}")
places.reverse()
print(f"list after 2nd places.reverse(): {places}")
print(f"list sorted(Places, reverse=True): {sorted(places, reverse=True)}")
print(f"\nlist Places current: {places}")
places.sort()
print(f"list after places.sort(): {places}")
print(f"\nlist Places current: {places}")
places.sort(reverse=True)
print(f"list after places.sort(reverse=True): {places}")
print(f"lenght of the list places: {len(places)}")

#task 3.6
print(f"print last value from the list places[-1]: {places[-1]}")

