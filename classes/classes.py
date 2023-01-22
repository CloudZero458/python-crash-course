class Dog:
    # "init" sets / assigns the data values for the object and is called when the the object is created
    #  "self" is  reference to the object that is created

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} rolled over')

my_dog = Dog('Noah', 3)
german_shepard = Dog('Pete', 10)


print(f'\nmy dog\'s name is {my_dog.name}.\n')
print(f'{my_dog.name} is {my_dog.age} years old')
my_dog.sit()
my_dog.roll_over()

print(f'\nThe german shepard\'s name is {german_shepard.name}.\n')
print(f'{german_shepard.name} is {german_shepard.age} years old')
german_shepard.sit()
german_shepard.roll_over()

''''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # attributes can be assigned default values making parameters unnecessary

    def full_name(self):
        full_name = f"\na {self.year} {self.make} {self.model}"
        return full_name.title()

    def read_odometer(self):
        print(f"\nThis car has {self.odometer} miles on it")

    def update_odometer(self, mileage):

    # when the function is called the parameter value for mileage is assigned to the odometer attribute
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # when the function is called the parameter value for miles is added to the existing value for the odometer attribute
        if miles >= self.odometer:
            self.odometer += miles
        else:
            print("You can't roll back an odometer!")
'''

my_car = Car('audi','r8','2016')
print(my_car.full_name())
my_car.read_odometer()

# modifying attribute values

#1
my_car.odometer = 25
my_car.read_odometer()

#2
''''
def update_odometer(self, mileage):
    # when the function is called the parameter value for mileage is assigned to the odometer attribute
    self.odometer = mileage
'''

my_car.update_odometer(150)
my_car.read_odometer()

#3
''''
def increment_odometer(self, miles):
        # when the function is called the parameter value for miles is added to the existing value for the odometer attribute
        self.odometer += miles
'''
my_car.increment_odometer(75)
my_car.read_odometer()

# inheritance
# the methods from the parent class are automatically inherited
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # inherits attributes from parent class
        self.battery = Battery()
        #self.battery_size = 40
    '''
    def describe_battery_size(self):
        print(f"\nThis car has a {self.battery_size}-kWh battery")
    '''



# composition - referencing objects from another class

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery_size(self):
        print(f"\nThis car has a {self.battery_size}-kWh battery")

    def get_range(self):

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"\nThis car has a range of about {range} miles on a full charge")

audi_etron = ElectricCar('audi', 'e-tron', 2015)
print(audi_etron.full_name())
audi_etron.battery.describe_battery_size()
audi_etron.battery.get_range()

#import multiple classes from a module
# from car import Car, ElecricCar

'''
import an entire module:

import car

# car is for "module", Car is for "class"

audi_r8 = car.Car('audi','r8',2016)

audi_etron = car.ElectricCar('audi','e-tron',2010)

'''
# import all classes from a module (not recomended due to name clash):

# from module_name *

# importing a module into a module:

from car import Car
from electric_car import ElectricCar

''''
using aliases:

from electric_car impot ElectricCar as EC # class alias

audi_etron = EC('audi','e-tron',2010)

import electric_car as ec # module alias

audi_etron = ec.ElectricCar('audi','e-tron',2010)

'''
'''
# python standard library:

from random import randint, choice

randint(1, 6) # a random number between 1 and 6

players = ['charles', 'martina', 'dave', 'eli', 'jasmine']

first_turn = choice(players) # chooses a random element
first_turn

'''
