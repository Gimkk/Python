#task10-11
import json
file_name = "number.json"

try:
    number = int(input("Enter number:"))
except ValueError:
    pass
else:
    with open(file_name, "w") as file:
        json.dump(number, file)

try:
    with open(file_name) as file:
        content = json.load(file)
except FileNotFoundError:
    print("you didn't enter any number")
else:
    print(f"i know your number is {content}")