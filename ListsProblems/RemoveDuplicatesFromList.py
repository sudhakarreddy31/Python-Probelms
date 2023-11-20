# How do you remove duplicates from Lists in place?


# list=[1,2,3,5,6,1,2]
# duplicates = []

# for i in list:
#     if i not in duplicates:
#         duplicates.append(i)

# print(duplicates)




def remove_duplicates_in_lists(list):
    lst=[]
    for i in list:
        if i not in lst:
            lst.append(i)
    return lst

ls=remove_duplicates_in_lists([1,2,3,4,2,3,6])
print(ls)






