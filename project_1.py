print("The menu is \nbreakfast_burrito - 4.50 \ncheeseburger - 4.00 \nhot dog - 3.00 \nteriyaki bowl - 5.00 \nchips - 1.00 \nfries - 2.50 \nsoda - 1.75 \nwater – 1.50")
menu = ["breakfast_burrito","cheeseburger","hot dog"," teriyaki bowl","chips" ,"fries" ,"soda","water"]

breakfast_burrito = 4.50
cheeseburger = 4.00
hot_dog = 3.00
teriyaki_bowl= 5.00
chips = 1.00
fries = 2.50
soda = 1.75
water = 1.50

total_amount = 0.0
for item in menu:
    order = input(f"Will you be ordering {item}?")    
    if order.strip().lower() == "yes":
        number = input("How many? Please enter a number: ")

    if item.lower() == "breakfast_burrito" and order.strip().lower() == "yes":
        total_amount = float(total_amount) + 4.50 * float(number)
        breakfast_burrito_ordered = True
    
    if item.lower() == "cheeseburger" and order.strip().lower() == "yes":
        total_amount = float(total_amount) + 4.00 * float(number)
        cheeseburger_ordered = True
    
    if item.lower() == "hot dog" and order.strip().lower() == "yes":
        total_amount = float(total_amount) + 3.00 * float(number)
        hot_dog_ordered = True
    
    if item.lower() == "teriyaki bowl" and order.strip().lower() == "yes":
        total_amount = float(total_amount) + 5.00 * float(number)
        terriyaki_bowl_ordered = True

    if item.lower() == "chips" and order.strip().lower() == "yes":
        total_amount = float(total_amount) + 1.00 * float(number)
        chips_ordered = True

    if item.lower() == "water" and order.strip().lower() == "yes":
        total_amount = float(total_amount) + 1.50 * float(number)
        water_ordered = True

print(total_amount)

