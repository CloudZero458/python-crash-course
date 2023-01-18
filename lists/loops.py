magicians = ["Harry Potter", "Voldemort", "Dumbledore"]

for magician in magicians:
  print(f"{magician} \n")


# send a message to each name in the list and capitalize each name
for magician in magicians:
    print(f"{magician.title()}, dark magic is the most powerful \n")
    print(f"I can't wait to see which side you choose {magician.title()} \n")

print("I wish you all well")

# list comprehension

magician = [magician.title() for magician in magicians]

print(magician)
