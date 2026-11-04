
# Part 1: Build the Database

stars = {
    "Sun": {"x": 0, "y": 0, "z": 0, "luminosity": 1.0, "mass": 1.0},
    "Sirius": {"x": -1.6, "y": 8.1, "z": -2.5, "luminosity": 25.4, "mass": 2.06},
    "Vega": {"x": 7.2, "y": -4.5, "z": 25.3, "luminosity": 40.0, "mass": 2.14},
    "Proxima Centauri": {"x": 1.6, "y": -3.8, "z": -1.2, "luminosity": 0.0017, "mass": 0.12},
    "Betelgeuse": {"x": 88.0, "y": -120.0, "z": 45.0, "luminosity": 100000.0, "mass": 16.5}
}

print("Number of stars:", len(stars))
print("Sirius mass:", stars["Sirius"]["mass"])

vega = stars["Vega"]
print("Vega is at", (vega["x"], vega["y"], vega["z"]))


# Part 2: Loop and Find the Average Mass

total_mass = 0

for name in stars:
    print(name + ": mass", stars[name]["mass"],
          ", luminosity", stars[name]["luminosity"])
    total_mass = total_mass + stars[name]["mass"]

average_mass = total_mass / len(stars)
print("Average mass:", average_mass)

brightest_star = ""
highest_luminosity = 0

for name in stars:
    if stars[name]["luminosity"] > highest_luminosity:
        highest_luminosity = stars[name]["luminosity"]
        brightest_star = name

print("Brightest star:", brightest_star)


# Part 3: Search and Update the Map

search_name = input("Which star do you want to look up? ").strip().title()

if search_name in stars:
    print(stars[search_name])
else:
    print("Star not found")

# Update Proxima Centauri's mass
stars["Proxima Centauri"]["mass"] = 0.122

# Add a new star
stars["Nova"] = {
    "x": 12.0,
    "y": 5.0,
    "z": 8.0,
    "luminosity": 15.0,
    "mass": 0.8
}

# Delete one star
del stars["Sun"]

print("Number of stars after update:", len(stars))

# Calculate the new average mass
total_mass = 0

for name in stars:
    total_mass = total_mass + stars[name]["mass"]

average_mass = total_mass / len(stars)
print("Updated average mass:", average_mass)


# Part 4: Observation Log, a List of Dictionaries

observation_log = [
    {"star": "Sirius", "night": 1, "clear_sky": True},
    {"star": "Vega", "night": 2, "clear_sky": True},
    {"star": "Proxima Centauri", "night": 3, "clear_sky": False}
]

for entry in observation_log:
    print("Night", entry["night"] + 0, ":", entry["star"],
          "(clear sky:", entry["clear_sky"], ")")
    print("Mass:", stars[entry["star"]]["mass"])

# Add another observation
new_star = input("Enter a star name to add to the observation log: ").strip().title()

if new_star in stars:
    new_entry = {
        "star": new_star,
        "night": 4,
        "clear_sky": True
    }
    observation_log.append(new_entry)
    print("Observation added.")
else:
    print("Star not found. Observation not added.")

print("Number of observations:", len(observation_log))


# Challenge: Find the Star Farthest from the Sun

farthest_star = ""
greatest_distance = 0

for name in stars:
    distance = (
        stars[name]["x"] ** 2
        + stars[name]["y"] ** 2
        + stars[name]["z"] ** 2
    ) ** 0.5

    if distance > greatest_distance:
        greatest_distance = distance
        farthest_star = name

print("Farthest star:", farthest_star)
print("Distance from Sun:", greatest_distance)
