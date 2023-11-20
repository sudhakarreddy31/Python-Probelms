# How to print all prime numbers up to a given number

number = eval(input("Enter A number : "))


for i in range(1,number+1):
    if number > 1:
        for j in range(2,i):
            if i % j ==0:
                break
        else:
            print(i)







