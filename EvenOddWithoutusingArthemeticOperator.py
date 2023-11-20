# How to check if a given number is even/odd without using the Arithmetic operator


def even_odd(number):
    return not(number & 1)

number = int(input("Enter A Number :"))
if even_odd(number):
    print("Given number is Even Number")
else:
    print("Given number is odd Number")
    