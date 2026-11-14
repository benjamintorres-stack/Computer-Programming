#Benjamin Torres
#Computer Programming p4
#Homework 6
#11 / 11 / 2026

group_size =  int(input("How many people are in your group"))
if group_size >= 8:
    print("Sorry, you must wait for a table")
elif group_size < 8:
    print("Your table is ready")
elif group_size <= 0:
    print("Please input a nonzero number")

number = float(input("Enter a number: "))
if number % 10 == 0:
    print("Your number is a multiple of 10.")
else:
    print("Your number is not a multiple of 10.")

topping = input("What topping would you like? Type quit to exit the loop")

while topping != "quit":
    print("I'll add ", topping , " to your pizza.")
    topping = input("What else would you like? ")
print("Your pizza is ready!")

age = input("Enter your age or quit: ")
while age != "quit":
    age = float(age)
    if age < 0 or age % 1 != 0:
        print("Please enter a valid age.")
    elif age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    age = input("Enter your age or quit: ")


sandwich_orders = ["tuna", "ham", "turkey", "chicken"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " , current_sandwich , " sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
sandwich_orders = ["pastrami", "tuna", "pastrami", "ham", "pastrami", "turkey"]

finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)

vacations = []
active = True
while active:
    place = input("Where would you go on vacation? ")
    vacations.append(place)
    answer = input("Another person? yes or no: ")
    if answer == "no":
        active = False
print("Dream vacation results:")
for place in vacations:
    print(place)