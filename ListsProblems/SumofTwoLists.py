# How do you find the sum of two lists 

# By Using zip()

list1 = [1,2,4,6]
list2 = [9,7,0,4]

sum_list = []

for i,j in zip(list1,list2):
    sum_list.append(i+j)

print("The Sum Of Two lists is :",sum_list)


# By using List Comphersion

lst1 = [7,8,3,2]
lst2 = [2,44,23,9]

lst_sum = [i + j for i,j in zip(lst1,lst2)]

print("The Sum Of Two lists is :",lst_sum)

