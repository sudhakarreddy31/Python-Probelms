# Given the two lists (names and populations), 
# combine them back into a list of dictionaries 
# using for loops... using list comprehensions.

names = ["Andhra Pradesh","Telanganna","Karanaka","Keralam"]
populations = [8912345,98989,798493,8498594,789898]

# for loop...

names_populations = []

for index,name in enumerate(names):
    town ={"name":name,"poplutions":populations[index]}
    names_populations.append(town)
print(names_populations)


# List comprehensions... 
towns = [{ 
    'name': town_name, 
    'population': populations[index] 
} for index, town_name in enumerate(names)] 
print(towns)
