# Using the list of towns, 
# find the total combined population using for loops...
# using the sum() function... using the reduce() function.



from functools import reduce


towns = [{'name': 'Manchester', 'population': 58241}, 
        {'name': 'Coventry', 'population': 12435}, 
        {'name': 'South Windsor', 'population': 25709}]

# For loops... 

total_populations = 0
for i in towns:
    total_populations += i.get('population')

print(total_populations)

# Sum function...

total_populations =  sum(i.get('population') for i in towns)
print("Total Populations Of Countries: ",total_populations)


# Reduce function... 
total_population = reduce(lambda total, town: total + town.get('population'), towns, 0)
print(total_population)


