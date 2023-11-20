# How to find the maximum occurring character in a given String?

string = "Hello how are you"
result = string.count('o')
print("The Number of Occurences is : ",result)

def maximum_number_occurence(string):
    string = string.count("n")
    return string

string = "Hello Chinna "
result = maximum_number_occurence(string)
print("The Number of Occurences is : ",result)



def max_occurence(str):
    dict = {}
    for i in str:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    return dict

str = "Helloo Pukoooo"
result = max_occurence(str)
print(result)








