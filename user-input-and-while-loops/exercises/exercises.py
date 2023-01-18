'''
favorite_car = input("What's your favorite car? ")

print(f'Your favorite car is an {favorite_car.title()}')

dinner = int(input("how many people did you go out to dinner with? "))

print(f'You went out to dinner with {dinner} people')

multipe_of_10 = int(input("Enter a number "))
if multipe_of_10 % 10 == 0:
    print(f'\n{multipe_of_10} is a multiple of 10')
else:
    print(f'\n{multipe_of_10} is not a multiple of 10')

'''

'''
active = True
while active:
    pizza_toppings = input("\nenter your favorite pizza toppings or enter \"ex\" to exit: ")

    if pizza_toppings == 'ex':
        active = False
    else:
        print(f'\n{pizza_toppings} will be added to your pizza')
'''
pizza_toppings = ""

while pizza_toppings != 'ex':
    pizza_toppings = input("\nenter your favorite pizza toppings or enter \"ex\" to exit: ")

    if pizza_toppings == 'ex':
        break
    else:
        print(f'\n{pizza_toppings} will be added to your pizza')
