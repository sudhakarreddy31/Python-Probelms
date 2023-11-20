# How are duplicates removed from an array without using any library in python

def remove_duplicates(input_lists):
    uniqui_lists=[]
    for i in input_lists:
        if i not in uniqui_lists:
            uniqui_lists.append(i)
    return uniqui_lists

input_lists=[1,2,7,0,5,6,2,4,1,]
result=remove_duplicates(input_lists)
print(result)













