# Find The Sum of Total in Given lists?

# Itereting through the loop

def sum_of_lists(input_list):
    total = 0
    for i in input_lists:
        total = total + i
    return total

input_lists = [10,5,20,40,10]
result = sum_of_lists(input_lists)
print("Sum Of Total List is :",result)

# Using Bulit-in Function

input_lists = [10,5,20,40,10]
result=sum(input_lists)
print(result)












