current_number = 1

print('\nCount to 5:\n')
while current_number <= 5:
    print(current_number)
    current_number+=1

print(f'\nThe current number is {current_number}. End of loop')

prompt = "\nEnter a word and I'll repeat it. Enter \"ex\" to exit: "

message = ""

# a flag is used if there are multiple conditions that can affect when the loop should end
active = True

while active:
    # show input prompt with message
    message = input(prompt)

    if message == "ex":
        active = False

    else:
        print(f'\n{message}')


# or
'''
message = ""
while message != 'ex':
    # show input prompt with message
    message = input(prompt)

    if message == "ex":
        break

    else:
        print(f'\n{message}')
'''


#only prints out the odd numbers.

print("\nPrinting odd numbers between 0 and 10:\n")
current_number = 0
while current_number < 10:
    current_number += 1 # iterate so the loop can end
    if current_number % 2 == 0:
        continue # the continue statement returns to the beginning of the loop
    print(current_number)


# moving items from one list to another

new_users = ['chris', 'brian','tiffany']

confirmed_users = []

# true if there's at least 1 item in the array
while new_users:
    current_user = new_users.pop()
    print(f'\nverifying user:\n\n{current_user.title()}\n')

    confirmed_users.append(current_user)


print('\nthe following users have been verified:\n')

for confirmed_user in confirmed_users:
    print(f'{confirmed_user.title()} \n')


# removing all instances of an item from a list


pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print('\npets:\n')
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print('\nremoving all instances of "cat" from the list:')
print(f'\n{pets}')

# filling a dictionary with user input

responses = {}


polling_active = True

#name = ""

#fav_car = ""

while polling_active:

    name = input('\nWhat is your name? type "x" to exit ')

    if name == 'x':
        #polling_active = False
        break

    fav_car = input('\nWhat is your favorite car? type "x" to exit ')

    if fav_car  == 'x':
        #polling_active = False
        break

    if name and fav_car != 'x' and name and fav_car:
        # store the response in the dictionary
        responses[name.title()] = fav_car.title()
        print('\npolling results:')
        for name, fav_car in responses.items():
            print(f'\n{name}\'s favorite car is an {fav_car}.')
