"""
Anagram is Both strings are equal length (or) if both string equal same order or differnt order 

example:
heart
earth

both strings are equal length

hello
helli

both are equal length but not equal charactors

"""


str1 = input("Enter a string :")
str2 = input("Enter a string :")


if len(str1) != len(str2):
    print("Not Angrams..")
else:
    if sorted(str1)==sorted(str2):
        print("Both Strings are Anagrams.")
    else:
        print("Not Anagrams...")














