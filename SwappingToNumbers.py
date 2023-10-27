# Write Program Swapping Two Number Using Temprary Variable 

# Apporach-1

NumberA = 100
NumberB = 50

print("Befour Swapping NumberA",NumberA)
print("Befour Swapping NumberB",NumberB)

temp = NumberA              # 100
NumberA = NumberB           # 50
NumberB = temp              # 100

print("After Swapping NumberA",NumberA)
print("After Swapping NumberB",NumberB)

# --------------------------------------------------------------------------------------------

# Write Program Swapping Two Number Using Temprary Variable  from User

# Apporach-2

NumberA = input("Enter Fisrt Number : ")
NumberB = input("Enter Second Number : ")


print("Befour Swapping NumberA",NumberA)
print("Befour Swapping NumberB",NumberB)

temp = NumberA              
NumberA = NumberB           
NumberB = temp              

print("After Swapping NumberA",NumberA)
print("After Swapping NumberB",NumberB)


# --------------------------------------------------------------------------------------------

# Apporch-3

Num1=56
Num2=20

Num1,Num2=Num2,Num1


print("After Swapping NumberA",Num1)
print("After Swapping NumberB",Num2)





















