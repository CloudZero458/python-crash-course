def make_pizza(size, *toppings):
    print(f'\nmaking a {size}-size pizza with the following toppings:\n')
    for topping in toppings:
        print(f'{topping}')
