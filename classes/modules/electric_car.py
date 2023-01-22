from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # inherits attributes from parent class
        self.battery = Battery()
        #self.battery_size = 40

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
