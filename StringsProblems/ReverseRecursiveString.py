# How can a given string be reversed using recursion?

def reverse_recursive(str):
    if len(str) == 1:
        return str
    else:
        return reverse_recursive(str[1:]) + str[0]
    

str = "amul"
result = reverse_recursive(str)
print(result)
