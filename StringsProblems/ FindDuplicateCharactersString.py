# How do you find duplicate characters in a given string? 


from collections import Counter

str = "hippopotamus"
word_length = Counter(str)
print(word_length)


def find_duplicates_charactors(string):
    word_length = Counter(string)

    for i,j in word_length.items():
        if j > 1:
            print(f"{i} is Happing {j} Times ")
            


string = "hippopotamus"
find_duplicates_charactors(string)
