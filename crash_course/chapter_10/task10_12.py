import json

file_name = "number.json"

def read_file(file_name):
    try:
        with open(file_name) as file:
            number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return number

def write_file(file_name):
    try:
        number = int(input("Enter number: "))
    except ValueError:
        return None
    else:
        with open(file_name, "w") as file:
            json.dump(number, file)
        return number

def print_number():
    number = read_file(file_name)
    if number:
        print(f"Your number is {number}")
    else:
        number = write_file(file_name)
        print(f"Your number is: {number}")

print_number()



