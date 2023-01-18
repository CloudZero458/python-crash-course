''''
note:

the first index includes the index you start at and everything to the right

the second index selects everything to the left of the index

'''

players = ["batman", "bruce", "spiderman", "peter", "superman", "clark","wolverine", "logan"]


# prints the item at index 3 and everything to the right
print(players[3:])


# prints  the 4th and 5th players ("peter and superman)
print(players[3:5])

# prints everything to the left of index 4
print(players[:2])

# start at the 3rd item from the end of the list, printing everything to the left
print(players[:-5])

# starts at the index 2, printing everything to the right of the list

print(players[2:])

#starts at the end of the list and prints the item at negative index 3 and everything to the right.         a negative index starts at 1.
print(players[-3:])

# using a third number skips certain items. in this example it will skip every 2nd name
print(players[0:6:2])

# looping through specific items
print("here are the first 3 players on my team: \n")

#starts at index 3 and prints everything to the right
for player in players[:3]:
  print(player.title())


# prints second, third and fourth items
for player in players[1:4]:
  print(player.title())

# makes a copy of a list
my_food = ["ramen", "buffalo wings", "tacos", "french fries"]

friends_food = my_food[:]

my_food.append("turkey wings")

friends_food.append("pizza")

print(f"my favorite foods are: {my_food}")
print(f"my friends' favorite foods are: {friends_food}")
