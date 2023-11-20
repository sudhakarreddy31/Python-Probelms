# Create a new list of the town names using for loops... using list comprehensions... using the map() function.


# For loops... 

towns = [{'name': 'Manchester', 'population': 58241}, 
        {'name': 'Coventry', 'population': 12435}, 
        {'name': 'South Windsor', 'population': 25709}]

towns_name = []

for i in towns:
    towns_name.append(i.get('name'))

print(towns_name)


# List comprehensions... 

towns_name = [i.get('population') for i in towns]
print(towns_name)


# Map function... 

towns_name = map(lambda i: i.get('name'),towns)
print(towns_name)

