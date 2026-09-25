#Torres, Benjamin
#Computer Programming P4
#Assignment 2b
#9 / 25 / 2026

alien_color = "green"
if alien_color=="green":
    print("You have earned five points!")
else:
    print("You have earned ten points!")
alien_color = ("yellow")
if alien_color=="green":
    print("You have earned five points!")
else:
    print("You have earned ten points!")

alien_color = "green"
if alien_color == "green":
    print("You have earned 5 points!")
elif alien_color == "yellow":
    print("You have earned 10 points!")
else:
    print("You have earned 15 points")

alien_color = "yellow"
if alien_color == "green":
    print("You have earned 5 points!")
elif alien_color == "yellow":
    print("You have earned 10 points!")
else:
    print("You have earned 15 points")

alien_color = "red"
if alien_color == "green":
    print("You have earned 5 points!")
elif alien_color == "yellow":
    print("You have earned 10 points!")
else:
    print("You have earned 15 points")

ages = [1, 3.9 , 10 , 13 , 19 , 20 , 21 , 65]
for age in ages:
    if age < 2:
        print("You are a baby")
    elif age < 4:
        print("You are a toddler")
    elif age < 13:
        print("You are a kid")
    elif age < 20:
        print("You are a teenager")
    elif age < 65:
        print("You are an adult")
    else:
        print("You are an elder")

users = ["admin" , "ben" , "john" , "jaden" , "sal"]
for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    elif users == []:
        print("The list is empty")
    else:
        print (f"Hello {user} thank you for logging in again.")
users = []
if users == []:
    print("The list is empty")
for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    elif users == []:
        print("The list is empty")
    else:
        print (f"Hello {user} thank you for logging in again.")
current_users = ["john", "maria", "ben", "alex", "james"]
new_users = ["JOHN", "sarah", "mike", "Ben", "luis"]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} will need to enter a new username.")
    else:
        print(f"{user} is available.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")