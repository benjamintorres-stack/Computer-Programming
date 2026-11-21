
# Torres Benjamin
# Computer Programming, period 4
# Assignment: Homework 7

# 1. T-Shirts

def make_shirt(size, message):
    print("The shirt size is " + size + " and the message is '" + message + "'.")

make_shirt("large", "Hello World")
make_shirt(size="medium", message="Python is cool")


# 2. T-Shirts Part 2

def make_shirt2(size="large", message="I love Python"):
    print("The shirt size is " + size + " and the message is '" + message + "'.")

make_shirt2()
make_shirt2("medium")
make_shirt2("small", "Hello!")


# 3. Cities

def describe_city(city, country="USA"):
    print(city + " is in " + country + ".")

describe_city("Los Angeles")
describe_city("New York")
describe_city("Tokyo", "Japan")


# 4. City Names

def city_country(city, country):
    return city + ", " + country

print(city_country("Santiago", "Chile"))
print(city_country("Los Angeles", "USA"))
print(city_country("Tokyo", "Japan"))


# 5. Album

def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}

    if songs != None:
        album["songs"] = songs

    return album

print(make_album("Drake", "Views"))
print(make_album("Kendrick Lamar", "DAMN."))
print(make_album("Tyler, The Creator", "IGOR"))
print(make_album("Travis Scott", "Astroworld", 17))


# 6. User Albums

while True:
    print("\nEnter album information (or type 'quit' to stop).")

    artist = input("Artist: ")

    if artist == "quit":
        break

    title = input("Album title: ")

    if title == "quit":
        break

    print(make_album(artist, title))


# 7. Messages

messages = [
    "Hello!",
    "How are you?",
    "Have a good day!"
]

def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)


# 8. Sending Messages

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)

messages = [
    "Hello!",
    "How are you?",
    "Have a good day!"
]

sent_messages = []

send_messages(messages, sent_messages)

print("Messages:", messages)
print("Sent messages:", sent_messages)


# 9. Archived Messages

messages = [
    "Hello!",
    "How are you?",
    "Have a good day!"
]

sent_messages = []

send_messages(messages[:], sent_messages)

print("Original messages:", messages)
print("Sent messages:", sent_messages)


# 10. Sandwiches

def make_sandwich(*items):
    print("\nYour sandwich will have:")
    for item in items:
        print(" This " + item)

make_sandwich("turkey", "cheese")
make_sandwich("ham", "lettuce", "tomato")
make_sandwich("chicken", "bacon", "cheese", "avocado")


# 11. Cars

def make_car(manufacturer, model, **options):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }

    for key, value in options.items():
        car[key] = value

    return car

car = make_car("subaru", "outback", color="blue", tow_package=True)

print(car)
