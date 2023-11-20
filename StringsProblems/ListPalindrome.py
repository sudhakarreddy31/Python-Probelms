# How to check if a given  list is a palindrome? 

def is_palindrome(input_list):
    return input_list == input_list[::-1]

input_list = [1,2,3,2,1]
result = is_palindrome(input_list)
print(result)

