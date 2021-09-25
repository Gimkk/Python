#task5-8
usernames = ["eric", "smith", "leo", "mark", "simon", "admin"]

for user in usernames:
    if user == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for login again.")

#task5-9

if usernames:
    for user in usernames:
        if user == "admin":
            print(f"\nHello {user}, would you like to see a status report?")
        else:
            print(f"\nHello {user}, thank you for login again.")
else:
    print("We need to find some users!")

#task5-10
current_users =["eric", "smith", "Leo", "mark", "simon", "admin"]
new_users = ["david", "michael", "leo", "francis", "ela", "peter"]

current_users_copy = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_copy:
        print("Need to enter new name")
    else:
        print(f"User name '{user}' is available")

#task5-11
numbers = [number for number in range(1,10)]
for number in numbers:
    if number == 1:
        print("1st")
    elif number ==2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
