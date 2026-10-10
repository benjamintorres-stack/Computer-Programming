input1 = input("Right or Left? ").strip()

# 1
if input1.lower() == "right":
    print("You've entered a haunted house. Your car is red.")
    x = input("Go upstairs or downstairs? ").strip()

    # 2
    if x.lower() == "downstairs":
        print("Not smart. You die. Game over.")

    # 3
    elif x.lower() == "upstairs":
        print("Good job! You find a door.")
        y = input("Go in or leave? ").strip()

        # 4
        if y.lower() == "leave":
            print("A ghost was waiting outside. You die.")

        # 5
        elif y.lower() == "in":
            treasure_chest = input("Open or leave the chest? ").strip()

            # 6
            if treasure_chest.lower() == "open":
                print("You found a key!")
                key = True

            # 7
            elif treasure_chest.lower() == "leave":
                print("You leave the chest behind.")
                key = False

            # 8
            else:
                print("Invalid choice. Game over.")
                key = False

            # 9
            if treasure_chest.lower() == "open" or treasure_chest.lower() == "leave":
                next_option = input("Path or woods? ").strip()
                
                # 10
                if next_option.lower() == "woods":
                    print("You get lost in the forest.")

                # 11
                elif next_option.lower() == "path":
                    print("You find a river blocking your way.")
                    river = input("Swim or build a raft? ").strip()

                    # 12
                    if river.lower() == "swim":
                        print("The current is too strong. Game over.")

                    # 13
                    elif river.lower() == "raft":
                        print("You cross the river safely.")
                        cave = input("Enter the cave or climb the hill? ").strip()

                        # 14
                        if cave.lower() == "enter the cave":
                            print("You find a sleeping dragon.")
                            dragon = input("Sneak past or wake it? ").strip()

                            # 15
                            if dragon.lower() == "wake it":
                                print("The dragon chases you away GAME OVER.")

                            # 16
                            elif dragon.lower() == "sneak past":
                                print("You sneak past the dragon.")
                                door = input("Open the wooden door or the iron door? ").strip()

                                # 17
                                if door.lower() == "wooden door":
                                    print("You find a room full of spiders. \nGAME OVER")

                                # 18
                                elif door.lower() == "iron door":
                                    print("You find a locked treasure room.")

                                    # 19
                                    if key == True:
                                        print("Your key unlocks the door!")
                                        treasure = input("Take the gold or the diamond? ").strip()

                                        # 20
                                        if treasure.lower() == "gold":
                                            print("You take the gold and win!")

                                        # 21
                                        elif treasure.lower() == "diamond":
                                            print("You take the diamond and win!")

                                        # 22
                                        else:
                                            print("Invalid choice. Game over.")

                                    # 23
                                    else:
                                        print("You don't have a key. The door stays locked.")

                                # 24
                                else:
                                    print("Invalid door. Game over.")

                            # 25
                            else:
                                print("Invalid choice. Game over.")

                        # 26
                        elif cave.lower() == "climb the hill":
                            print("You reach the top and see your car!")
                            car = input("Run to the car or explore the tower? ").strip()

                            # 27
                            if car.lower() == "run to the car":
                                car_color = input("What color was your car?").strip()
                                if car_color.lower() == "red":
                                    print("You win!")
                                else:
                                    print("Wrong, GAME OVER")
                

                            # 28
                            elif car.lower() == "explore the tower":
                                print("You find a secret room and win!")

                            # 29
                            else:
                                print("Invalid choice. Game over.")

                        # 30
                        else:
                            print("Invalid choice. Game over.")

                    else:
                        print("Invalid choice. Game over.")

                else:
                    print("Invalid choice. Game over.")

        else:
            print("Invalid choice. Game over.")

    else:
        print("Invalid choice. Game over.")

elif input1.lower() == "left":
    print("You find an abandoned cabin.")
    print("You die. Game over.")

else:
    print("Invalid choice. Please enter Right or Left.")