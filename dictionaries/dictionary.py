alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])

print(alien_0["points"])

# assigning value from dictionary to a variable

points = alien_0["points"]
print(points)

# adding key values to a dictionary

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# changing values in a dictionary

alien_0["color"] = "silver"
print(alien_0)

alien_0 = {'color': 'silver', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\ncurrent x-position: {alien_0['x_position']}")
# moves the alien "x" pixels to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
print(f'x_increment is: {x_increment}')
# new position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"new x-position: {alien_0['x_position']}")

# remove a key/value
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'devin': 'rust',
    'phil': 'python',
    }

# assign a key/value to a variable
language = favorite_languages['sarah']

# using get() allows you to return a default value if the key doesn't exist

alien_0 = {'color': 'silver','x_position': 0, 'y_position': 25, 'speed': 'medium'}

points = alien_0.get('points', 'no point value assigned')
print(points)
