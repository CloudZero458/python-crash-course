# tuples are immutable lists (lists that can't be changed)


numbers = (200, 50,25,75)

# tries to change a value in the tuple but can't
# dimensions[0] = 250

#a tuple needs a trailing comma, even with a single value
single_value = (1,)


for number in numbers:
  print(number)

# replaces /overwrites the numbers tuple above
numbers = (100, 45, 36, 85)

for number in numbers:
  print(number)
