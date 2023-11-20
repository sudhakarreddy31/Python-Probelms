# How do you print the first non-repeated character from a string?

# By using Count Function 

string = input("Enter A String : ")
nonrepeat=False

for charactor in string:
    if (string.count(charactor)) == 1:
        print("The First Non Repeating Charactor in String is : ",charactor)
        nonrepeat=True
        break

if nonrepeat == False:
    print("No Non-Repeating Charactors")



# By using Count Function 

def non_repeating_charactor(string):
    for i in string:
        if string.count(i) == 1:
            print("The First Non Repeating Charactor is : ",i)
            break

strindaing=non_repeating_charactor("india")







