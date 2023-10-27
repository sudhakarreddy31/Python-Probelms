# Write Fibonacci Series Program

"""
    A Series of Numbers in which each Number the sum two Precending Numbers is Konw Fibonacci Series

    Example :
    0,1,2,3,4
    0+1=1
    1+1=2
    2+2=4
    4+3=7
    7+4=11


"""
# ====================================================================================================


Number1=0
Number2=1
for i in range(2,10):
    sum = Number1+Number2
    print(sum)
    Number1 = Number2
    Number2 = sum


# ====================================================================================================

Number1=1
Number2=2

list=[]
for i in range(2,10):
    sum = Number1+Number2
    list.append(sum)
    Number1 = Number2
    Number2 = sum

print(list)




# ====================================================================================================


numA=int(input("Enter A First Number is : "))
numB=int(input("Enter A Second Number is : "))

for i in range(0,numB+1):
    add = numA + numB
    numA = numB
    numB = add
    print(add)

# ====================================================================================================
