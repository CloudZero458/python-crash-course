players = ["batman", "bruce", "spiderman", "peter", "superman", "clark","wolverine", "logan"]

print(f"The first 3 items in the list are: {players[:3]}")

print(f"The 2 items in the middle are: {players[3:5]}")
print(f"The last 3 items are: {players[-3:]} \n")

my_pizza = ["cheese pizza", "pepporoni pizza"]

friends_pizza = my_pizza[:]

my_pizza.append("philly cheesesteak pizza")

friends_pizza.append("taco pizza")

print(f"my favorite pizzas are: \n")
for pizza in my_pizza:
  print(f"{pizza} \n")

print("my friend's favorite pizzas are: \n")
for pizza in friends_pizza:
  print(f"{pizza} \n")



my_food = ["ramen", "buffalo wings", "tacos", "french fries"]

friends_food = my_food[:]

my_food.append("turkey wings")

friends_food.append("pizza")

print(f"My favorite foods are: \n")
for food in my_food:
  print(f"{food}")

print(f"\nMy friend's favorite foods are: \n")
for food in friends_food:
  print(f"{food}")

buffet = ("steak","pie", "salad", "french fries", "mashed potatoes")
print("\noriginal menu: \n")

for food in buffet:
  print(food)
# tries to change the tuple
#buffet[-1] = "baked potato"

buffet = ("steak","turkey wings", "tacos", "french fries", "mashed potatoes")
print("\nrevised menu: \n")

for food in buffet:
  print(food)
