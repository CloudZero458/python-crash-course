requested_toppings = ["pepperoni","extra cheeese", "bacon", 'green peppers']

for topping in requested_toppings:
    if topping == "green peppers":
        print("Sorry, we're all out of green peppers.")
    else:
        print(f"adding {topping}.")

print("\nFinished making your pizza!\n")

requested_toppings = []

# checks if the list has at least 1 item
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?\n")


# using multiple lists

requested_toppings = ["pepperoni","extra cheeese", "tacos", 'sesame chicken']

available_toppings = ["pepperoni","extra cheeese", "bacon", 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print("this topping is not available")
print("\nFinished making your pizza")
