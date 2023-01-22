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

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # inherits attributes from parent class
        self.battery = Battery()


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
