# Create two lists, one of the town names and one of the town populations using for loops... 
# using list comprehensions... 
# using the zip() function.

# For loops... 
towns = [{'name': 'India', 'population': 58241},
        {'name': 'Chinna', 'population': 12435}, 
        {'name': 'South Sudan', 'population': 25709}]

town_names = []
town_populations =[]

for i in towns:
    town_names.append(i.get('name'))
    town_names.append(i.get('population'))
print(town_names,)


# List comprehensions... 

town_names = [i.get('name') for i in towns]
town_populations =[i.get('population') for i in towns]
print(town_names,town_populations)


# Zip function... 

town_names,town_populations = zip(*[(i.get('name'),i.get('population'))for i in towns])
print(town_names,town_populations)



















