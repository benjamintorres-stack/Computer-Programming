#Torres, Benjamin
#Computer Programming P4
#Assignment 2a
#September 10 2026

hobbies = ["football","Rocket League","Watching CFB","Watching NFL","Minecraft"]
print(hobbies)
print(len(hobbies))
print(hobbies[2])
print(hobbies[0])

hello = ["hello "*100]
print(hello)

list_1 = ["pumpkin","halloween","jack-o-lantern","spooky"]
list_2 = ["christmas","holiday","new year","santa"]
print(list_1+list_2)

favFoods = ["Tacos","Sandwiches","Burger","Fries","Steak"]
print(len(favFoods))
print(favFoods[2])
print(favFoods[-5])
favFoods.append("Ben")
favFoods.insert(2,17)
favFoods.pop(0)
print(favFoods)

numbers = list(range(0,21))
print(numbers)
numbers = list(range(1,21,2))
print(numbers)

animals = ["dog", "cat", "rabbit"]

for animal in animals:
    print(animal)
    print("A "+ animal +" would make a great pet.")
print("Any of these animals would make a great pet!")

guests = ["LeBron James", "Lionel Messi", "Trent Williams"]
for guest in guests:
    print("I would like to invite " + guest + " to dinner.")
    guests = ["LeBron James", "Lionel Messi", "Trent Williams"]

print(guests[1] + " can't make it to dinner.")

guests[1] = "Cristiano Ronaldo"

for guest in guests:
    print("I would like to invite " + guest + " to dinner.")