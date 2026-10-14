print("The menu is \nbreakfast_burrito - 4.50 \ncheeseburger - 4.00 \nhot dog - 3.00 \nteriyaki bowl - 5.00 \nchips - 1.00 \nfries - 2.50 \nsoda - 1.75 \nwater - 1.50")

menu = ["breakfast_burrito", "cheeseburger", "hot dog", "teriyaki bowl", "chips", "fries", "soda", "water"]

# quantities
burrito_quantity = 0
cheeseburger_quantity = 0
hot_dog_quantity = 0
teriyaki_quantity = 0
chips_quantity = 0
fries_quantity = 0
soda_quantity = 0
water_quantity = 0

total_amount = 0

for item in menu:
    order = input(f"Will you order {item}? ")

    if order.strip().lower() == "yes":
        number = int(input("How many? Please enter a number: "))

        if item == "breakfast_burrito":
            total_amount += 4.50 * number
            burrito_quantity = number

        elif item == "cheeseburger":
            total_amount += 4.00 * number
            cheeseburger_quantity = number

        elif item == "hot dog":
            total_amount += 3.00 * number
            hot_dog_quantity = number

        elif item == "teriyaki bowl":
            total_amount += 5.00 * number
            teriyaki_quantity = number

        elif item == "chips":
            total_amount += 1.00 * number * 1.10
            chips_quantity = number

        elif item == "fries":
            total_amount += 2.50 * number * 1.10
            fries_quantity = number

        elif item == "soda":
            total_amount += 1.75 * number * 1.10
            soda_quantity = number

        elif item == "water":
            total_amount += 1.50 * number * 1.10
            water_quantity = number


# RECEIPT
print("\nItem              Quantity     Base Amount     Total Amount")
print("-----------------------------------------------------------")

if burrito_quantity > 0:
    print(f"Breakfast Burrito   {burrito_quantity}          $4.50          ${4.50*burrito_quantity}")

if cheeseburger_quantity > 0:
    print(f"Cheeseburger        {cheeseburger_quantity}          $4.00          ${4.00*cheeseburger_quantity}")

if hot_dog_quantity > 0:
    print(f"Hot Dog             {hot_dog_quantity}          $3.00          ${3.00*hot_dog_quantity}")

if teriyaki_quantity > 0:
    print(f"Teriyaki Bowl       {teriyaki_quantity}          $5.00          ${5.00*teriyaki_quantity}")

if chips_quantity > 0:
    print(f"Chips               {chips_quantity}          $1.00          ${(1.00*chips_quantity)*1.10}")

if fries_quantity > 0:
    print(f"Fries               {fries_quantity}          $2.50          ${(2.50*fries_quantity)*1.10}")

if soda_quantity > 0:
    print(f"Soda                {soda_quantity}          $1.75          ${(1.75*soda_quantity)*1.10}")

if water_quantity > 0:
    print(f"Water               {water_quantity}          $1.50          ${(1.50*water_quantity)*1.10}")

print("-----------------------------------------------------------")
print(f"Your total is: ${total_amount}")


# PAYMENT
payment = input("What type of payment? (cash/cub cash): ")

if payment.lower() == "cash":
    cash = float(input("Enter cash amount: "))
    change = cash - total_amount
    print(f"Change returned: ${change}")
    print("Thank you!")

elif payment.lower() == "cub cash":
    balance = 100 - total_amount
    print("Thank you for using Cub Cash!")
    print(f"Your remaining balance is: {balance}")