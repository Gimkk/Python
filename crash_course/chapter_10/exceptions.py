try:
    print(5/0)
except ZeroDivisionError:
    print("Divid by zero is not allowed")
else:
    print("it worked")

#task10-6
print("\n---Enter number once ---")

try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
except ValueError:
    print("Enter number only")
else:
    print(f"some of two numbers: {num1 + num2}")

#task10-7
print("\n---Enter number in while loop ---")
while True:
    try:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
    except ValueError:
        print("Enter number only")
    else:
        print(f"some of two numbers: {num1 + num2}")
        break