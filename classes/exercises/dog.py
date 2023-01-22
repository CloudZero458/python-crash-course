class Dog:
    def __init__(self, name, age): # init is called when the the object is created
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
