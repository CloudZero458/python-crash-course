from car import Car

my_new_car = Car('audi', 'r8', 2016)
print(my_new_car.full_name())

my_new_car.odometer = 23

my_new_car.read_odometer()
