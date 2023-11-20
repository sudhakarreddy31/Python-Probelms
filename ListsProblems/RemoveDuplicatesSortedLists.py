# How to remove duplicates from a sorted linked list? 

def remove_duplicate_sorted_list(sorted_list):
    return list(set(sorted_list))


sorted_list = [1,1,1,2,3,3,4,5]
result = remove_duplicate_sorted_list(sorted_list)
print(result)







