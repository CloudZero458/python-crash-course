cars = ['audi', "bmw", "mercedes", "porsche"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

topping = "pepporoni"

if topping != "anchovies":
    print("hold the anchovies")

guess_the_number = 15

if guess_the_number != 7:
    print("wrong answer")

# using "and" to check if 2 or more conditions are true

age_1 = 16

age_2 = 21

if age_1 >= 21 and age_2 >= 21:
    print("true")
else:
    print("false")

#or
if (age_1 >= 21) and (age_2 >= 21):
    print("true")
else:
    print("false")

if age_1 >= 21 or age_2 >= 21:
    print("true")
else:
    print("false")

# checks if value exists
requested_toppings = ["pepperoni","bacon", "onions", "pineapple"]


if "pepperoni" in requested_toppings:
    print("add pepporoni")

if "mushrooms" not in requested_toppings:
    print("no mushrooms")

banned_users = ["andrew", "caroline", "david"]

user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response.")

age = 17

if age >= 18:
    print("you are old enough to vote")
else:
    print("You are too young to vote")

age = 12

if age < 4:
    print("Your cost of admission is free")
elif age < 18:
    print("Your cost of admission is $25")
elif age >= 65:
    print("Your cost of admission is $20")
else:
    print("Your cost of admission is $40")

# or

age_2 = 19

if age_2 < 4:
    price = 0
elif age_2 < 18:
    price = 25
elif age_2 >= 65:
    price = 20
else:
    price = 40
print(f"Your cost of admission is ${price}.")

# else ststement is removed

age_3 = 65

if age_3 < 4:
    price = 0
elif age_3 < 18:
    price = 25
elif age_3 < 65:
    price = 40
elif age_3 >= 65:
    price = 20
print(f"Your cost of admission is ${price}.")

# multiple if statements
requested_toppings = ["pepperoni","bacon", "onions", "pineapple"]

if "pepperoni" in requested_toppings:
    print("adding pepperoni")
if "bacon" in requested_toppings:
    print("adding bacon")

if "extra cheese" in requested_toppings:
    print("adding extra cheese")

print(f"\nFinished making your pizza!")
