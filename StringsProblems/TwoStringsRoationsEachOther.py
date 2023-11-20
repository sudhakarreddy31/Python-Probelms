# How do you check if two strings are a rotation of each other? 

def roation_each_other(str1,str2):
    if len(str1) != len(str2):
        return False
    
    temp = str1 + str1

    if str2 in temp:
        return True
    else:
        return False
    

str1 = "rotation"
str2 = "tionrota"

if roation_each_other(str1,str2):
    print("The strings are rotation each other")
else:
    print("The strings are not rotation each other")


