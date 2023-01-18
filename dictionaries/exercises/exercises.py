person = {
    'first_name': 'Ryan',
    'last_name': 'Burrow',
    'age': 33,
    'height': '5 foot 7.5',
    'race': 'black',
    'city': 'baltimore',
    }

print (person)

favorite_numbers = {
    'person1': 33,
    'person2': 25,
    'person3': 48,
    'person4': 17,
    'person5': 22,
    }

for key, value in favorite_numbers.items():
   print(f"{key}'s favorite number is {value}.")


glossary = {
    'variable': 'a reference to a value',
    'function': 'a piece of code that completes a specific action',
    'list': 'a collection of data types',
    'tuple': 'a list that can\'t be changed',
    'dictionary': 'a collection of related data',
    }

for key, value in glossary.items():
    print(f"a {key} is {value}")

rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Lena': 'Russia'
    }
print("\nrivers:\n")
for river, country in rivers.items():
    print(f"The {river} river runs through {country}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'devin': 'python',
    'phil': 'java',
    }

favorite_language_poll = ['joe', 'dave', 'devin', 'jasmine', 'phil']
print("\nfavorite language poll:\n")
for name in favorite_language_poll:
    if name in favorite_languages:
        print(f"{name.title()}, thanks for taking the poll.")
    else:
        print(f"{name.title()} can you take the poll?")



people = {
    'ryan': {
        'first_name': 'ryan',
        'last_name': 'burrow',
        'age': 33,
        'height': '5 foot 7.5',
        'race': 'black',
        'city': 'baltimore',
        },
    'raiden': {
        'first_name': 'raiden',
        'last_name': 'x',
        'age': 300,
        'height': '6 foot 5',
        'race': 'white',
        'city': 'unknown',
        },
    'subzero': {
        'first_name': 'subzero',
        'last_name': 'x',
        'age': 33,
        'height': '5 foot 9',
        'race': 'asian',
        'city': 'unknown',
        },
    }
print("\npeople:\n")
for name, info in people.items():
    full_name = f"Full name: {info['first_name'].title()} {info['last_name'].title()}\n"
    age = f"\nAge: {info['age']}\n"
    height = f"\nHeight: {info['height']}\n"
    race = f"\nRace: {info['race']}\n"
    city = f"\nCity {info['city'].title()}\n"
    print(f"{full_name}{age}{height}{race}{city}")

pets = {
    'pet_1': {
        'name': 'Noah',
        'species': 'dog',
        'age':3,
        'color': 'black and brown',

        },
    'pet_2': {
        'name': 'hawk',
        'species': 'bird',
        'age':4,
        'color': 'black, red and brown',

        },
    'pet_3': {
        'name': 'king',
        'species': 'tiger',
        'age':7,
        'color': 'orange and black',

        },
    }

print("\nPets:\n")
for pet, pet_info in pets.items():
    name = f"name: {pet_info['name'].title()}\n"
    species = f"species: {pet_info['species']}\n"
    age = f"age: {pet_info['age']}\n"
    color = f"color: {pet_info['color']}\n"
    print(f"{name}{species}{age}{color}")
