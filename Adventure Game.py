input1 = input("Right or Left").strip()
#2
if input1.lower() == "right":
    print("You've entered a haunted house, your car is red")
    x = input("You must chose,\nGo Upstairs to a well lit room \nGo downstairs into a dark basement \nUpstairs or Downstairs").strip()
elif input1.lower() == "left":
    print("You die \ngame over")
#4
if x.lower() == "downstairs":
    print("Not smart \nYou die \nGame over")
elif x.lower() == "upstairs":
     print("Good job, You find a door")
     print("Do you go in or leave")
     y = input("In or Leave?").strip()
#6
if y.lower() == "leave":
    print("a ghost was waiting outside \nYou Die \nGame OVER")
else:
    treasure_chest = input("You keep going in a hallway \nYou find a chest, do you open it or leave it? \nOpen or Leave?").strip()
#8
if treasure_chest.lower() == "open":
    print("you found a key!")
    key = True
elif treasure_chest.lower() == "leave":
    print("who knows what you missed")
    key = False
#10
next_option = input("You stumble out of the house into the forrest.\nYou have to find your way back\nGo on the path or go through the woods? \n Path or Woods?").strip()
if next_option.lower() == "woods":
    print("You got lost \nGame Over")
elif next_option.lower() == "path":
    print("Nice")