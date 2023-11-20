# How to remove the duplicate character from String?

def remove_duplicates_string(string):
    str = ''
    for i in string:
        if i not in str:
            str=str + i
    return str

string = 'abcaadcefgh'
result = remove_duplicates_string(string)
print(result)









