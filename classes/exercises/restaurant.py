class Restaurant:


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'\n{self.restaurant_name} serves {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        print(f'\n{self.restaurant_name} is now open.')

bungiorno = Restaurant('Bungiorno', 'Italian')

taco_bell = Restaurant('Taco Bell', 'Mexican')

golden_city = Restaurant('Golden City', 'Asian')

print(f'\n{bungiorno.restaurant_name}')
print(f'\n{bungiorno.cuisine_type}')

bungiorno.describe_restaurant()
bungiorno.open_restaurant()

taco_bell.describe_restaurant()
taco_bell.open_restaurant()

golden_city.describe_restaurant()
golden_city.open_restaurant()
