# How do you find duplicate numbers in an array if it contains multiple duplicates? 

list = [1,2,2,3,4,5,5,6,7,1]

unique_lists = []
duplicates_lists = []

for i in list:
    if i not in unique_lists:
        unique_lists.append(i)

    elif i not in duplicates_lists:
        duplicates_lists.append(i)


print("Duplicates Elements are ",duplicates_lists)


def duplicates_lists(lists):
    unique_lists = []
    duplicates_lists =[]

    for i in lists:
        if i not in unique_lists:
            unique_lists.append(i)

        elif i not in duplicates_lists:
            duplicates_lists.append(i)

    return duplicates_lists

lists=[1,2,2,3,4,5,5,6,7,1]
list = duplicates_lists(lists)
print(list)








