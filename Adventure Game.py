input1 = input("Right or Left")

if input1.lower() == "right":
    print("You've entered a haunted house")
    x = input("You must chose,\nGo Upstairs to a well lit room \nGo downstairs into a dark basement \nUpstairs or Downstairs")
else:
    print("You die \ngame over")
#2
if x.lower() != "upstairs":
    print("Not smart \nYou die \nGame over")
else:
     print("Good job, You find a door")
     print("Do you go in or leave")
     y = input("In or Leave?")
#4
if y.lower() == "in":
    