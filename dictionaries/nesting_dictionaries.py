# a list of dictionaries

alien_0 = {'color': 'green', 'points': 5,}
alien_1 = {'color': 'yellow', 'points': 10,}
alien_2 = {'color': 'red', 'points': 15,}

aliens = [alien_0, alien_1, alien_2]
print("\naliens:\n")
for alien in aliens:
    print(alien)

aliens = []

# create 30 aliens and store in the "aliens" list
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5,'speed': 'slow',}
    aliens.append(new_alien)

# print first 5 aliens
print("\nthe first 5 aliens are:\n")
for alien in aliens[:5]:
    print(alien)

print(f"\nThe total number of aliens are: {len(aliens)}")

# looping through "aliens" list and changing values for the first 3 aliens

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print("\nfirst 5 aliens:\n")
for alien in aliens[:5]:
    print(alien)

# a list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['pepporoni', 'extra cheese'],
    }

print("\n pizza:\n")
print(f"You ordered a {pizza['crust']}-crust pizza with {pizza['toppings'][0]} and {pizza['toppings'][1]}.")

#or
'''
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(topping)
'''
favorite_languages = {
    'jen': ['python', 'c'],
    'sarah': ['c'],
    'devin': ['python', 'go'],
    'phil': ['java', 'haskell'],
    }
print("\nlanguages:\n")

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is {languages}")
    else:
        print(f"{name.title()}'s favorite languages are:\n")
        # loop through the values
        for language in languages:
            print(language.title())
    print("\n")

# a dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
    }

for username, user_info in users.items():
    print(f"\nusername: {username}")

    full_name = f"full name: {user_info['first'].title()} {user_info['last'].title()}."
    location = f"location: {user_info['location'].title()}."
    print(f"\n{full_name}\n{location}")
