def hello():
    print(f"hello world!")


hello()


def greeting(name):
    print(f"hello {name.title()}")


greeting("ryan")

# positional arguments


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type} named {pet_name.title()}")


describe_pet("dog", "noah")

# keyword arguments. the order doesn't matter


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type} named {pet_name.title()}")


describe_pet(pet_name="noah", animal_type="dog")

# default value. position matters so default parameters have to be after regular parameters


def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type} named {pet_name.title()}")


describe_pet("noah")

# return values. return values return a function's output
"""

def name_format(first_name, last_name):
    full_name = f"\n{first_name} {last_name}"
    return full_name.title()


# print(name_format('a','b'))

name = name_format("ryan", "burrow")

print(name)


# optional arguments
# parametes with default values are always last


def name_format(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"

    else:
        full_name = f"\n{first_name} {last_name}"
    return full_name.title()


name = name_format("ryan", "burrow")

name = name_format("ryan", "burrow", "curtis")  # remember parameters with default values are alway last

print(name)

"""


def name_format_2(first_name, last_name, middle_name="", age=None):

    if middle_name and age:
        full_name_0 = f"\n{first_name} {middle_name} {last_name}"
        full_name = full_name_0.title()
        age = str(age)
        message = f"{full_name} is {age} years old."
        return message

    elif middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
        return full_name.title()

    elif age:
        full_name_0 = f"\n{first_name} {last_name}"
        full_name = full_name_0.title()
        age = str(age)
        message = f"{full_name} is {age} years old."
        return message

    else:
        full_name_0 = f"\n{first_name} {last_name}"
        full_name = full_name_0.title()
        return full_name


name = name_format_2("ryan", "burrow", "curtis")
print(name)
name = name_format_2("ryan", "burrow", age=34)
print(name)
name = name_format_2("ryan", "burrow", "curtis", age=34)
print(name)
name = name_format_2("ryan", "burrow")
print(f'{name} \n')


# returning a dictionary

def build_person(first, last):
    person = {
        "first_name": f'{first.title()}',
        "last_name": f'{last.title()}',
    }  # parameters are assigned as values

    return person



person = build_person("ryan", "burrow")

print('returning dictionary:\n')
print(person)

#  using a function and a for loop on a dictionary
print('\nusing a function and a for loop on a dictionary:\n')
def build_person(first, last):
    person = {
        "first_name": f'{first.title()}',
        "last_name": f'{last.title()}',
    }  # parameters are assigned as values




    msg = []
    for name, value in person.items():
        n = name
        v = value

        print(f'{n}:\n{v}') # using return doesn't work

person = build_person("ryan", "burrow")

print(person)




# using a function with a while loop


def name_formatter(first, last):
    full_name = f"{first} {last}"
    return full_name


while True:
    print('\nwhat is your first name? (enter "x" to quit)')
    first = input(f"\nfirst name: ")

    if first == "x":
        break

    last = input("\nlast name: ")
    if last == "x":
        break

    name = name_formatter(first, last)  # pass in values from the while loop to the function

    print(f"\nyour name is: {name.title()}")

# passing a list

def greet_users(names):
    for name in names:
        msg = f'Hello, {name.title()}'
        print(msg)

uernames = ['hannah','dave','jake']

greet_users(uernames)

# modifying a list in a function

list_1 = ['a','b','c','d']

list_2 = []

# true if list contains at least 1 item
while list_1:
    store = list_1.pop()
    list_2.append(store)
    print(f'adding item {store} to list 2')

print('\nitems in list 2:\n')
for items in list_2:
    print(items)

def move_items(list_1, list_2):
    while list_1:
        store = list_1.pop()
        list_2.append(store)
        print(f'adding item {store} to list 2')

def print_items(list_2):

    for items in list_2:
        print(items)

list_1 = ['a','b','c','d']

list_2 = []

move_items(list_1[:], list_2) # [:] sends a copy of the list
print('\nitems in list 2:\n')
print_items(list_2)
print(f'\nlist 1: {list_1}\n')

#####################################

# passing an  arbitrary /unknown amount of arguments to a function

def make_pizza(*toppings):
    print(f'{toppings}\n')


# results ar printed out as tuples
make_pizza('pepporoni')
make_pizza('extra cheese','green peppers', 'bacon')

def make_pizza(*toppings):
    for topping in toppings:
        print(f'\n{topping}')

make_pizza('pepporoni')
make_pizza('extra cheese','green peppers', 'bacon')

#####################################

# positional and arbitrary arguments

# the parameter that accepts arbitrary arguments must be placed last

def make_pizza(size, *toppings):
    print(f'\nmaking a pizza with {size}-inch pizza with the following toppings:\n')
    for topping in toppings:
        print(f'{topping}')

print('\n')

make_pizza(12,'pepporoni')
make_pizza(16,'extra cheese','green peppers', 'bacon')

#####################################################

# arbitrary keyword arguements( ex: make_pizza(topping='pepperoni'))

def build_profile(first, last, **user_info):

    #referencing the **user_info parameter and adding the first_name and last_name parameter to the user_info parameter
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

print('\nAlbert Einstein\'s profile:\n')

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

#####################################################

# using "as" to give a function or a module an alias
'''
from pizza import make_pizza as mp

mp(16, 'pepporoni')

import pizza as p

p.make_pizza(16, 'pepporoni')

# imports all functions
from pizza import *

make_pizza(16, 'pepporoni')

'''
########################################
