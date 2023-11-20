# How do you print the Repeated character from a string?



string = input("Enter A String: ")    
repeating_char= set()


for charactor in string:
    if (string.count(charactor) > 1):
        repeating_char.add(charactor)

print("The Repeating Charactors in String ",repeating_char)
