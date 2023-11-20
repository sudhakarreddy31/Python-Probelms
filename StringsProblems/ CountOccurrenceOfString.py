# How do you count the occurrence of a given character in a string?


def count_occurance_in_string(string,occurence):
    count = 0
    for char in string:
        if char == occurence:
            count += 1
    return count
    

input_string = "Hello Chinna How Are You..!"
count_of_occerance= 'o'
result=count_occurance_in_string(input_string,count_of_occerance)
print(result)