places = ["Spain", "Africa", "Portugal","Bahamas", "Moldova"]

print(f"list: {places} \n")

print(f"alphabetical order (temporary): {sorted(places)} \n")

print(f"list: {places} \n")

print(f"reverse alphabetical order (temporary): {sorted(places, reverse=True)} \n")

print(f"list: {places} \n")

places.reverse()
print(f"reverse order (permanent): {places} \n")

places.reverse()
print(f"original order (permanent): {places} \n")

places.sort()
print(f"alphabetical order (permanent): {places} \n")

places.sort(reverse=True)
print(f"reverse alphabetical order (permanent): {places} \n")

print(f"{len(places)}")
