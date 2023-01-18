user_0 = {
    'username': 'raiden357',
    'first_name': 'Ryan',
    'last_name': 'Burrow',
    }

for key, value in user_0.items():
    print(f"\nkey: {key}\nvalue: {value}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'devin': 'python',
    'phil': 'java',
    }


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through the keys in a dictionary. you can omit the keys() function since looping through the keys is the default behavior when you pass in a single argument.

print("\nkeys:")
for name in favorite_languages.keys():
    print(name.title())

# using conditonals when looping through a dictionary

friends = ['sarah','devin']

for name in favorite_languages:

    # if a name in favorite_languages matches a name in friends
    if name in friends:
        # the current value of the "name" variable is passed in as the key and it's value is assigned to the "language" variable
        language = favorite_languages[name].title()
        print(f"Hi {name.title()}, {language.title()} is your favorite language")
    else:
        print(f"Hi {name.title()}.")

# a loop is not necessary to access all the keys. The default behavior is to return all the keys.
if 'joe' not in favorite_languages:
    print("Joe please take the poll.")

# looping through keys in alphabetical order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thanks for taking the poll")

# looping through values in a dictionary
print("\nfavorite languages:\n")
for language in favorite_languages.values():
    print(f"{language.title()}")

# skips duplicates
print("\nremoving duplicates:\n")
for language in set(favorite_languages.values()):
    print(language.title())


# dictionary comprehension
person_0 = {'first': first_name.title(), 'last':last_name} # parameters ae assigned as values

person = {(first,last.title()) for first, last in person_0.items()}
         # {first.title():last.title() for first, last in person_0.items()}

print(person)
