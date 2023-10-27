"""
    Factorial Number is Multiple itself

    Example :
    5! = 5 * 4 * 3 * 2 * 1

    0! is 1

"""

# By Using looping Statment

factorial = 1
number = int(input("Enter A Number : "))    #5

for i in range(1,number+1):                 #5+1=6
    factorial = factorial * i

print(factorial)



# By Using Recursive Function

def factorial(Number):
    if Number == 0 or Number == 1:
        return 1 
    else:
        return Number * factorial(Number-1)


Number=factorial(5)
print(Number)


