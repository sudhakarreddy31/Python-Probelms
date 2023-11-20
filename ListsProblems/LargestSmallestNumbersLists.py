# How do you find the largest and smallest number in an unsorted integer array? 


def largest_smallest_number(list):
    lst=[]
    largest = max(list)  
    smallest = min(list)
    lst.append(largest)
    lst.append(smallest)

    return lst


list=[1,4,33,667,7,12,98]
result = largest_smallest_number(list)
print("largest and smallest numbers are :",result)








