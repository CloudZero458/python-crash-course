twenty = [num for num in range(1,21)]
print(f"range of 20: {twenty} \n")

#or
twenty = []
for num in range(1,21):
  twenty.append(num)

print(f"range of 20: {twenty} \n")

# or
one_hundred = [num for num in range(1, 101)]
print(f"smallest number in a range of 100: {min(one_hundred)} \n")
print(f"largest number in a range of 100: {max(one_hundred)} \n")
print(f"the sum of all the numbers in a range of 100: {sum(one_hundred)} \n ")

odd = [num for num in range(1,21,2)]
print(f"odd number in a range of 20: {odd} \n")

# or
odd = []
for num in range(1,21,2):
  odd.append(num)

print(f"odd number in a range of 20: {odd} \n")

threes = [num * 3 for num in range(3,31)]
print(f"multiples of 3: {threes} \n")

threes = []

for num in range(3,31):
  threes.append(num * 3)

print(f"multiples of 3: {threes} \n")

cubes = [cube **3 for cube in range(1,11)]
print(f"numbers cubed in a range of 10: {cubes} \n")

cubes = []

for cube in range(1,11):
  cubes.append(cube **3)

print(f"numbers cubed in a range of 10: {cubes} \n")
