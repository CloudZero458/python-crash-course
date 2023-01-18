
# print from 1 up to, but not including 6
for value in range(1,6):
  print(value)

# convert the range of numbers to a list
numbers = list(range(1,6))
print(numbers)

# the third number adds to the numbers generated in the range
even_numbers = list(range(2, 15, 2))
print(even_numbers)

odd_numbers = list(range(3,24, 2))
print(odd_numbers)

# return the value of each number times itself
square_numbers = [number **2 for number in range(1,11) ]

print(square_numbers)

# or

'''
square_numbers = []

for number in range(1,11):
  square_numbers.append(number **2)

print(square_numbers)
'''


# or
'''
square_numbers = []

for num in range(1,11):
  square = num ** 2
  square_numbers.append(square)

print(squared_numbers) '''

digits = list(range(1,25))

# smallest number
print(min(digits))


# largest number
print(max(digits))

# the sum of all the numbers
print(sum(digits))
