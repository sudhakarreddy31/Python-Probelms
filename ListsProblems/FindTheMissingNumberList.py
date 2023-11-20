# How do you find the missing number in a given integer array of 1 to 100?

numbers = [1,2,4,5,6,7,8,9,10]

n = len(numbers)+1
totalsum = n*(n+1) // 2


sum = 0
for i in numbers:
    sum = sum +i

print("Missing number Is : ",totalsum - sum)















