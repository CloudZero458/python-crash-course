bicycles = ['trek','cannondale', 'redline', 'specialized']

print(bicycles[0])

# prints the last item in the list
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

names = ['Ryan','raiden','Recca']
print(names[0])

print(names[1].title())
print(names[2])

print(f"Wassup {names[0]}")
print(f"Wassup {names[1].title()}")
print(f"Wassup {names[2]}")

cars = ['Audi R8', ' Porsche Turbo 992 PDK', ' McLaren 625C']

#.join converts the list to a string. the delimeter ' ' seperates the items in the list
print(f"I want these cars: {','.join(cars)}")

# modifying elements in a list:

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# replace /modify an item in a list. replaces honda with ducati
motorcycles[0] = 'ducati'
print(motorcycles)

# adding items to the end of a list
motorcycles = ['ducati','yamaha','suzuki']
motorcycles.append('honda')
print(motorcycles)

# adding items to a list
motorcycles = ['ducati','yamaha','suzuki']
motorcycles.insert(2, 'honda')
print(motorcycles)

# remove an item using del
motorcycles = ['ducati','yamaha','suzuki']
del motorcycles[1]
print(motorcycles)

# remove an item using pop. by default this removes an item from the end of a list. use pop() when you want to use the deleted item (ex. storing it in a variable)
motorcycles = ['ducati','yamaha','suzuki']
print(motorcycles)
removed_motorcycle = motorcycles.pop()
print(removed_motorcycle)

# using pop to remove an item from any position in a list .

motorcycles = ['honda','ducati','yamaha','suzuki']
print(motorcycles)

favorite_motorcycle = motorcycles.pop(1)
print(f" my favorite motorcycle is {favorite_motorcycle.title()}")

# removing an item by value
motorcycles = ['honda','ducati','yamaha','suzuki']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

# permanently sorting by alphabetical order

cars = ['Audi R8', 'Porsche Turbo 992 PDK', 'McLaren 625C']
cars.sort()

# reverse alphabetical order
cars = ['Audi R8', 'Porsche Turbo 992 PDK', 'McLaren 625C']
cars.sort(reverse=True)

# temporarily sorting in alphabetical order
cars = ['Audi R8', 'Porsche Turbo 992 PDK', 'McLaren 625C']

sorted(cars)

# temporarily sorting in reverse alphabetical order
cars = ['Audi R8', 'Porsche Turbo 992 PDK', 'McLaren 625C']
sorted(cars, reverse=True)

# reverse the order of a list. apply a second time to revert to original order
cars = ['Audi R8', 'Porsche Turbo 992 PDK', 'McLaren 625C']
cars.reverse()
print(cars)

# access the last item in a list
cars[-1]

# find the length of a list
len(cars)
