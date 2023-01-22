from car import ElectricCar

audi_etron = ElectricCar('audi','etron', 2010)
print(audi_etron.full_name())
audi_etron.battery.describe_battery_size()
audi_etron.battery.get_range()
