# Print The Prime Number 1 to 50 

"""
Prime Number Nothing But A Number Diviable By 1 and itself Only Is Called "Prime Number"

Example : 

19 is Diviable Only 1 and Itself only 

28 is Divable By 1,2,4,7,28

"""


for i in range(1,51):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)




# Print The Prime Number 1 to 20 The Result in List Form


lst=[]
for i in range(1,21):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            lst.append(i)
print(lst)



# Check The Number is Prime Number or Not ?


foo = int(input("Enter A Number : "))

for i in range(2,foo):
    if foo % 2 == 0:
        print(f"{foo} is Not Prime Number..!")
        break
    else:
        print(f"{foo} is Prime Number..!")




