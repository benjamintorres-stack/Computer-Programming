# Last name, First name
# Computer Programming, period 4
# Assignment: Homework 4a
# Date 10 / 26 / 26

#Part A

person = {
    "first name" : "John",
    "last name" : "Smith",
    "age" : 17,
    "city" : "LA"
}
print(person)

aboutMe = {
    "name" : "Benjamin Torres",
    "age" : 17,
    "favFood" : "tacos",
    "hariColor" : "black",
    "favSubject" : "math",
    "favSweet" : "cookies",
    "favHobbies" : "football",
    "likeCoding" : True
}
print(aboutMe)

phonebook = {
"John" : 938477566,
"Jack" : 938377264,
"Jill" : 947662781
}
phonebook["Jake"] = 48585367
del phonebook["Jill"]
print(phonebook)

#Part B
glossary = {
    "Appeasement" : " Political, material, or territorial concessions to an aggressive power in order to avoid armed conflict.",
    "Gubernatorial" : "Relating to a state governor or the office of a governor in the United States.",
    "Mercantilism" : "An economic theory and nationalist policy from the 16th to the 18th centuries that aimed to maximize a nation's wealth and power by forcing a favorable balance of trade, accumulating precious metals, and heavily regulating the economy.",
    "Nihilism" : "A philosophical stance asserting that life, existence, and the universe are inherently lacking in objective meaning, purpose, or intrinsic values.",
    "Absurdism" : "A philosophical theory stating that the universe is irrational and meaningless, and that human beings suffer a fundamental conflict when they constantly search for order or meaning in a silent, indifferent world."
}
for k,v in glossary.items():
    print(k, "is defined as:", v ,"\n")

glossary["Ontological"] = "The philosophical study of being, existence, and the basic categories of reality."
glossary["Atemporal"]="Independent of, unaffected by, or free from the limitations of time."
glossary["Sempitemporal"]="Everlasting or eternal"
glossary["Cosmological"]="The scientific or philosophical study of the origin, structure, evolution, and fate of the universe."
glossary["Teleological"]="An approach that explains things by their end, purpose, or goal"

for k,v in glossary.items():
    print(k, "is defined as:", v ,"\n")

rivers = {
    "Nile" : "Egypt",
    "Amazon" : "Brazil",
    "Mississippi" : "The United States"
}
for k,v in rivers.items():
    print("The", k , "runs through" , v)
for k in rivers.keys():
    print(k)
for v in rivers.values():
    print(v)

person1 = {
    "firstName" : "Emilio",
    "lastName" : "Torres",
    "favColor" : "Black",
    "birthMonth" : "January"
}
person2 = {
    "firstName" : "Brendan",
    "lastName" : "Vanis",
    "favColor" : "Blue",
    "birthMonth" : "February"
}

person3 = {
    "firstName" : "Abby",
    "lastName" : "Quezada",
    "favColor" : "Green",
    "birthMonth" : "June"
}

people = [person1,person2,person3]
for x in people:
    print(x)

cities = {
    "Los Angeles": {
        "country": "United States",
        "population": 3800000,
        "fact": "Hollywood is located here"
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Tokyo has one of the busiest train systems in the world"
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "The Eiffel Tower is located here"
    }
}

for k, v in cities.items():
    print(k)
    print(v)