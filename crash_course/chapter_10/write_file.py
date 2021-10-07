#task10-3

file_path = 'guest.txt'
with open(file_path, 'w') as file_object:
    file_object.write(input("what is your name: "))

#task10-4
file_path = 'guest_book.txt'
with open(file_path, 'w') as file_object:
    while True:
        guest_name = input("Enter your name press q to quit: ")
        if guest_name == "q":
            break
        else:
            print(f"Welcome {guest_name}")
        file_object.write(guest_name + "\n")

#task10-5
file_path = 'poll.txt'
with open(file_path, 'w') as file_object:
    while True:
        poll = input("why you like programming? q to quit: ")
        if poll == "q":
            break
        else:
            file_object.write(poll + "\n")