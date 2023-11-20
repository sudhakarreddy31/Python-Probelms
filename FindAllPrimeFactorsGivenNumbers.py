# How to find all prime factors of a given number


number = int(input("Enter A number : "))

for i in range(1,number+1):
    if number%i == 0:
        print(i)