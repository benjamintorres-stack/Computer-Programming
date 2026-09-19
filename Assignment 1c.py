#Benjamin Torres
#Assignment 1c

#Part 1
name_of_object = input("Enter the name of the object")
mass_kg = input("what\'s the mass of the object in kg?")
velocity = input("What\'s the velocity of the object in m/s")

name_of_object_clean = name_of_object.strip().title()
mass_kg_number = float(mass_kg)
velocity_number = float(velocity)

KE_Joules = 1/2 * mass_kg_number * (velocity_number**2)
KE_Calories = KE_Joules/4.184
KE_ergs = KE_Joules * 10 ** 7

#print("Kinetic Energy Report for:", name_of_object)
output_line_one = f"Kinetic Energy Report for: {name_of_object}"
print(output_line_one)
print("--------------------------------------")
output_line_three = f"Joules: \t{KE_Joules} J"
print(output_line_three)
output_line_four = f"Calories:\t{KE_Calories} cal"
print(output_line_four)
output_line_five = f"Ergs:\t{KE_ergs} ergs"
print(output_line_five)