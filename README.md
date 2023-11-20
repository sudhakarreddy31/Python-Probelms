# Python Interview Coding Questions

Python Coding Questions With Solutions

### 1.Print Given Number is Even Or Odd Number?

```py
n = eval(input('Enter A Number: '))

if n%2==0:
    print("{} Is Even Number".format(n))
else:
    print("{} Is Odd Number".format(n))

Output:
Enter A Number: 5
5 Is Odd Number

```

### 2.Print First 10 Even Numbers Or Postive Numbers?

```py
for i in range(1,21):
    if i % 2 == 0:
        print("The Even Numbers are : ",i)

Output:
The Even Numbers are :  2
The Even Numbers are :  4
The Even Numbers are :  6
The Even Numbers are :  8
The Even Numbers are :  10
The Even Numbers are :  12
The Even Numbers are :  14
The Even Numbers are :  16
The Even Numbers are :  18
The Even Numbers are :  20

```
### 3.Print Even Numbers In 0 to 50 in List form?


```py
list=[]
for i in range(0,51,2):
    list.append(i)

print(list)

Output:

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

```


### 4.Print Factorial Number?

```py

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

Output:
Enter A Number : 5
120

# By Using Recursive Function

def factorial(Number):
    if Number == 0 or Number == 1:
        return 1 
    else:
        return Number * factorial(Number-1)


Number=factorial(5)
print(Number)


Output: 
120

```

### 5.Write Fibonacci Series Program?

```py
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

Number1=0
Number2=1
for i in range(2,10):
    sum = Number1+Number2
    print(sum)
    Number1 = Number2
    Number2 = sum

Output
1
2
3
5
8
13
21
34
------------------
Number1=1
Number2=2

list=[]
for i in range(2,10):
    sum = Number1+Number2
    list.append(sum)
    Number1 = Number2
    Number2 = sum

print(list)

Output:
[3, 5, 8, 13, 21, 34, 55, 89]


```
### 6.Print The Prime Numbers 1 to 50 ?

```py
"""
Prime Number Nothing But A Number Diviable By 1 and itself Only Is Called "Prime Number"

Example : 

19 is Diviable Only 1 and Itself only 

28 is Divable By 1,2,4,7,28

"""

for i in range(1,1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)

Output:
2
3
5
7

```

### 7.Write Program Swapping Two Number Using Temprary Variable 

```py
NumberA = input("Enter Fisrt Number : ")
NumberB = input("Enter Second Number : ")


print("Befour Swapping NumberA",NumberA)
print("Befour Swapping NumberB",NumberB)

temp = NumberA              
NumberA = NumberB           
NumberB = temp              

print("After Swapping NumberA",NumberA)
print("After Swapping NumberB",NumberB)

Output:
Enter Fisrt Number : 31
Enter Second Number : 18

Befour Swapping NumberA 31
Befour Swapping NumberB 18

After Swapping NumberA 18
After Swapping NumberB 31

```
### 8.How do you swap two numbers without using the third variable?
```py

Number1 = input("Enter a first number : ")
Number2 = input("Enter a Second number : ")

print("Befour swaping Number : ",Number1)
print("Befour swaping Number : ",Number2)

Number1,Number2 = Number2,Number1

print("After swaping Number : ",Number1)
print("After swaping Number : ",Number2)

Output:
Enter a first number : 88
Enter a Second number : 67

Befour swaping Number :  88
Befour swaping Number :  67

After swaping Number :  67
After swaping Number :  88

```

### 9.How do you check if two rectangles overlap with each other? 
```py

class Rectangle():

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def rectangle_overlap(rect1,rect2):
    if rect1.x1 >= rect2.x2 or rect2.x1 >=rect1.x2:
        return False

    
    if rect1.y1 >= rect2.y2 or rect2.y1 >= rect2.y1:
        return False

    return True


rect1 = Rectangle(0, 0, 2, 2)
rect2 = Rectangle(2, 5, 2, 0)

overlap = rectangle_overlap(rect1,rect2)

if overlap:
    print("Rectangle is Overlap")

else:
    print("Rectangle is do not overlap")


Output:
Rectangle is do not overlap

```

### 10.How to add two numbers without using the plus operator
```py
number1 = int(input("Enter First Number:"))
number2 = int(input("Enter Second Number:"))

add = number1 - (-number2)
print("Add Two Numbers Without using plus operator:",add)

OutPut:
Enter First Number:31
Enter Second Number:9
Add Two Numbers Without using plus operator: 40

```
### 11.How to print all prime numbers up to a given number
```py
number = eval(input("Enter A number : "))

for i in range(1,number+1):
    if number > 1:
        for j in range(2,i):
            if i % j ==0:
                break
        else:
            print(i)

OutPut:
Enter A number : 20
1
2
3
5
7
11
13
17
19

```
### 12.How to calculate the square root of a given number?
```py
number = int(input("Enter a number:"))
result = number ** 0.5
print(result)
import math
 number = 25
 result = math.sqrt(number)
 print(result)

OutPut:
Enter a number:9
3.0
5.0

```
### 13.How to convert a decimal number to binary 
```py
How to convert a decimal number to binary 

decimal_number = 4
decimal_number = bin(decimal_number)
print(decimal_number)

OutPut:
0b100

```
### 14.How to check if a given number is even/odd without using the Arithmetic operator
```py
def even_odd(number):
    return not(number & 1)

number = int(input("Enter A Number :"))
if even_odd(number):
    print("Given number is Even Number")
else:
    print("Given number is odd Number")
    

OutPut:
Enter A Number :6
Given number is Even Number

Enter A Number :7
Given number is Odd Number

```

### 15.How to check if a given number is positive or negative in Python?

```py

number = eval(input("Enter A Number: "))

if number > 0:
    print(f"{number} is a pastive Number..")
elif number < 0:
    print(f"{number} is Negative Number..")
else:
    print(f"{number} is Zero")

OutPut:
Enter A Number: 2
2 is a pastive Number..

Enter A Number: -6
-6 is Negative Number..

Enter A Number: 0
0 is Zero

```

### 16.How to reverse a given Integer in Python?

```py
Numbers = 1,2,3,5,431,418,19
result = Numbers[::-1]
print(result)


OutPut:
(19, 418, 431, 5, 3, 2, 1)
```
### 17.How to find all prime factors of a given number
```py
number = int(input("Enter A number : "))

for i in range(1,number+1):
    if number%i == 0:
        print(i)

OutPut:
Enter A number : 24
1
2
3
4
6
8
12
24

```




String Problems:
-----------------

### 18.Write A Palindrom Program?

```py
string = input("Enter A Sting :" ).lower()

if string == string[::-1]:
    print(f"{string} Is Palindrome")
else:
    print(f"{string} Is  Not Palindrome")


Output:
Enter A Sting :madam
madam Is Palindrome
```

### 19.How do you count the occurrence of a given character in a string?
```py

def count_occurance_in_string(string,occurence):
    count = 0
    for char in string:
        if char == occurence:
            count += 1
    return count
    

input_string = "Hello Chinna How Are You..!"
count_of_occerance= 'o'
result=count_occurance_in_string(input_string,count_of_occerance)
print(result)

Output:
3
```

### 20.How do you print the first non-repeated character from a string?
```py

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

Output:
Enter A String : india
The First Non Repeating Charactor in String is :  n


# By using Count Function 

def non_repeating_charactor(string):
    for i in string:
        if string.count(i) == 1:
            print("The First Non Repeating Charactor is : ",i)
            break

strindaing=non_repeating_charactor("india")
Output:
The First Non Repeating Charactor is :  n

```

### 21.Find The Lenth of Given String ?
```py
Name = "Sudhakar Reddy Moola"
print(len(Name))

Output:
20

list=[]
name = "Sudhakar Reddy Moola"
Name = name.split()
print(Name)

for i in Name:
    length = len(i)
    list.append(length)

print(list)

Output:
['Sudhakar', 'Reddy', 'Moola']
[8, 5, 5]

```

### 22.How do you check if two strings are anagrams of each other? 

```py

"""
Anagram is Both strings are equal length (or) if both string equal same order or differnt order 

example:
heart
earth

both strings are equal length

hello
helli

both are equal length but not equal charactors

"""


str1 = input("Enter a string :")
str2 = input("Enter a string :")


if len(str1) != len(str2):
    print("Not Angrams..")
else:
    if sorted(str1)==sorted(str2):
        print("Both Strings are Anagrams.")
    else:
        print("Not Anagrams...")

OutPut:
Enter a string :heart
Enter a string :earth
Both Strings are Anagrams.
--------------------------------------------------
Enter a string :hello
Enter a string :helli
Not Anagrams...

```

### 23.How to convert a byte array to String? 
```py
"""
UTF-8--->It stands for "Unicode Transformation Format - 8-bit" 
and is a variable-width encoding that can represent every character in the Unicode character set using one to four bytes.

"""


input_byte = b'Hello, This is input Array'

result = input_byte.decode('utf-8')

print(result)

OutPut:
Hello, This is input Array

```

### 24.How to find the maximum occurring character in a given String?
```py
string = "Hello how are you"
result = string.count('o')
print("The Number of Occurences is : ",result)

def maximum_number_occurence(string):
    string = string.count("n")
    return string

string = "Hello Chinna "
result = maximum_number_occurence(string)
print("The Number of Occurences is : ",result)



def max_occurence(str):
    dict = {}
    for i in str:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    return dict

str = "Helloo Pukoooo"
result = max_occurence(str)
print(result)

OutPut:
The Number of Occurences is :  3
The Number of Occurences is :  2
{'H': 1, 'e': 1, 'l': 2, 'o': 6, ' ': 1, 'P': 1, 'u': 1, 'k': 1}

```

### 25.How to find the maximum occurring character in a given String?
```py

string = "Hello how are you"
result = string.count('o')
print("The Number of Occurences is : ",result)

def maximum_number_occurence(string):
    string = string.count("n")
    return string

string = "Hello Chinna "
result = maximum_number_occurence(string)
print("The Number of Occurences is : ",result)



def max_occurence(str):
    dict = {}
    for i in str:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    return dict

str = "Helloo Pukoooo"
result = max_occurence(str)
print(result)

OutPut:
True
```

### 26.How do you find duplicate characters in a given string? 

```py

from collections import Counter

str = "hippopotamus"
word_length = Counter(str)
print(word_length)


def find_duplicates_charactors(string):
    word_length = Counter(string)

    for i,j in word_length.items():
        if j > 1:
            print(f"{i} is Happing {j} Times ")
            


string = "hippopotamus"
find_duplicates_charactors(string)

OutPut:

Counter({'p': 3, 'o': 2, 'h': 1, 'i': 1, 't': 1, 'a': 1, 'm': 1, 'u': 1, 's': 1})

p is Happing 3 Times 
o is Happing 2 Times 

```

### 27.How to remove the duplicate character from String?
```py

def remove_duplicates_string(string):
    str = ''
    for i in string:
        if i not in str:
            str=str + i
    return str

string = 'abcaadcefgh'
result = remove_duplicates_string(string)
print(result)

OutPut:
abcdefgh

```

### 28.How do you print the Repeated character from a string?
```py
string = input("Enter A String: ")    
repeating_char= set()


for charactor in string:
    if (string.count(charactor) > 1):
        repeating_char.add(charactor)

print("The Repeating Charactors in String ",repeating_char)

OutPut:
Enter A String: sudhakarreddy
The Repeating Charactors in String  {'r', 'a', 'd'}

```
### 29.How can a given string be reversed using recursion?
```py

def reverse_recursive(str):
    if len(str) == 1:
        return str
    else:
        return reverse_recursive(str[1:]) + str[0]
    

str = "amul"
result = reverse_recursive(str)
print(result)

OutPut:
luma

```
### 30.Print The Reverse String
```py
str = "Sudhakar Reddy"
str = str[::-1]
print(str)

OutPut:
yddeR rakahduS


# By Using Function

def reverse_string(s):
    return s[::-1]

s="Gayatri"
s=reverse_string(s)
print(s)

OutPut:
irtayaG

# Print Reverse Sentance

intro = "Hello My Self Sudhakar Reddy, I have Past 2 years in Python/Django Developer"

intro=intro[::-1]
print(intro)

OutPut:
repoleveD ognajD/nohtyP ni sraey 2 tsaP evah I ,yddeR rakahduS fleS yM olleH



# Print Reverse String Using Split Function

selff = "Hi How Are You..! , Where You From"

words = selff.split()
words = words[::-1]
print(words)

OutPut:
['From', 'You', 'Where', ',', 'You..!', 'Are', 'How', 'Hi']

```

### 31.How do you check if a string contains only digits? 
```py

string = "431418"
str=string.isdigit()
print(str)

OutPut:
True

str = "431.418"
string=str.isdigit()
print(string)

OutPut:
False

stringg = "123msr"
str1=stringg.isdigit()
print(str1)

OutPut:
False

```

### 32.How do you check if two strings are a rotation of each other? 

```py


def roation_each_other(str1,str2):
    if len(str1) != len(str2):
        return False
    
    temp = str1 + str1

    if str2 in temp:
        return True
    else:
        return False
    

str1 = "rotation"
str2 = "tionrota"

if roation_each_other(str1,str2):
    print("The strings are rotation each other")
else:
    print("The strings are not rotation each other")

OutPut:
The strings are rotation each other

```

### 33.How do you find the sum of two lists 

```py

# By Using zip()

list1 = [1,2,4,6]
list2 = [9,7,0,4]

sum_list = []

for i,j in zip(list1,list2):
    sum_list.append(i+j)

print("The Sum Of Two lists is :",sum_list)

OutPut:
The Sum Of Two lists is : [10, 9, 4, 10]



# By using List Comphersion

lst1 = [7,8,3,2]
lst2 = [2,44,23,9]

lst_sum = [i + j for i,j in zip(lst1,lst2)]

print("The Sum Of Two lists is :",lst_sum)

OutPut:
The Sum Of Two lists is : [9, 52, 26, 11]

```
### 34.Find Sum Of Elements List

```py
"""
    Sum Of Elements mean total sum in list
"""

list = [1,2,3,4,5]
print(sum(list))
OutPut:
15

# add one more value to output

list = [1,2,3,4,5]
print(sum(list,12))

OutPut:
27


# substact one more value to output

list = [1,2,3,4,5]
print(sum(list,-10))

OutPut:
5
```

### 35.How to check if a given  list is a palindrome? 

```py

def is_palindrome(input_list):
    return input_list == input_list[::-1]

input_list = [1,2,3,2,1]
result = is_palindrome(input_list)
print(result)

OutPut:
True

```
### 36.How do you sort a  list 

```py

def sort_list(input_list):
    return sorted(input_list)

input_list = [89,445,2,5,1,7,23,76,34,31,2,3,2,1,2]
result = sort_list(input_list)
print(result)

OutPut:
[1, 1, 2, 2, 2, 2, 3, 5, 7, 23, 31, 34, 76, 89, 445]

```

### 37.How do you reverse List in place in Python?
```py
list=[1,2,3,4,5,6]

list=list[::-1]
print(list)

OutPut:
[6, 5, 4, 3, 2, 1]

def reverse_list(list):
    return list[::-1]

lst = reverse_list([1,2,3,4])
print(lst)

OutPut:
[4, 3, 2, 1]

def reverse_list(list):
    return list[::-1]

lst = reverse_list(['1,2,3,4','msr',1,2,3])
print(lst)

OutPut:
[3, 2, 1, 'msr', '1,2,3,4']

```
### 38.ow to remove duplicates from a sorted linked list? 
```py
def remove_duplicate_sorted_list(sorted_list):
    return list(set(sorted_list))

sorted_list = [1,1,1,2,3,3,4,5]
result = remove_duplicate_sorted_list(sorted_list)
print(result)

OutPut:
[1, 2, 3, 4, 5]

```

### 39.How are duplicates removed from an array without using any library in python

```py
def remove_duplicates(input_lists):
    uniqui_lists=[]
    for i in input_lists:
        if i not in uniqui_lists:
            uniqui_lists.append(i)
    return uniqui_lists

input_lists=[1,2,7,0,5,6,2,4,1,]
result=remove_duplicates(input_lists)
print(result)

OutPut:
[1, 2, 7, 0, 5, 6, 4]

```

### 40. How do you remove duplicates from Lists in place?
```py
list=[1,2,3,5,6,1,2]
duplicates = []
for i in list:
    if i not in duplicates:
        duplicates.append(i)print(duplicates)

def remove_duplicates_in_lists(list):
    lst=[]
    for i in list:
        if i not in lst:
            lst.append(i)
    return lst

ls=remove_duplicates_in_lists([1,2,3,4,2,3,6])
print(ls)

OutPut:
[1, 2, 3, 4, 6]

```
### 41.How do you find duplicate numbers in an array if it contains multiple duplicates? 

```py

list = [1,2,2,3,4,5,5,6,7,1]

unique_lists = []
duplicates_lists = []

for i in list:
    if i not in unique_lists:
        unique_lists.append(i)

    elif i not in duplicates_lists:
        duplicates_lists.append(i)


print("Duplicates Elements are ",duplicates_lists)

OutPut:
Duplicates Elements are  [2, 5, 1]


def duplicates_lists(lists):
    unique_lists = []
    duplicates_lists =[]

    for i in lists:
        if i not in unique_lists:
            unique_lists.append(i)

        elif i not in duplicates_lists:
            duplicates_lists.append(i)

    return duplicates_lists

lists=[1,2,2,3,4,5,5,6,7,1]
list = duplicates_lists(lists)
print(list)

OutPut:
[2, 5, 1]

```

### 42.How do you find the largest and smallest number in an unsorted integer array? 

```py


def largest_smallest_number(list):
    lst=[]
    largest = max(list)  
    smallest = min(list)
    lst.append(largest)
    lst.append(smallest)

    return lst


list=[1,4,33,667,7,12,98]
result = largest_smallest_number(list)
print("largest and smallest numbers are :",result)

OutPut:
largest and smallest numbers are : [667, 1]

```
### 43.How do you find the missing number in a given integer array of 1 to 100?
```py

numbers = [1,2,4,5,6,7,8,9,10]

n = len(numbers)+1
totalsum = n*(n+1) // 2


sum = 0
for i in numbers:
    sum = sum +i

print("Missing number Is : ",totalsum - sum)

OutPut:
Missing number Is :  3

```
### 44.Find The Sum of Total in Given lists?
```py
# Itereting through the loop

def sum_of_lists(input_list):
    total = 0
    for i in input_lists:
        total = total + i
    return total

input_lists = [10,5,20,40,10]
result = sum_of_lists(input_lists)
print("Sum Of Total List is :",result)

OutPut:
Sum Of Total List is : 85

# Using Bulit-in Function

input_lists = [10,5,20,40,10]
result=sum(input_lists)
print(result)

OutPut:
85

```
### 45.Create a new list of the town names using for loops... using list comprehensions... using the map() function.

```py


# For loops... 

towns = [{'name': 'Manchester', 'population': 58241}, 
        {'name': 'Coventry', 'population': 12435}, 
        {'name': 'South Windsor', 'population': 25709}]

towns_name = []

for i in towns:
    towns_name.append(i.get('name'))

print(towns_name)

OutPut:
['Manchester', 'Coventry', 'South Windsor']

# List comprehensions... 

towns_name = [i.get('population') for i in towns]
print(towns_name)

OutPut:
[58241, 12435, 25709]

# Map function... 

towns_name = map(lambda i: i.get('name'),towns)
print(towns_name)

OutPut:
<map object at 0x7f90aebcf130>

```

### 46.Create two lists, one of the town names and one of the town populations using for loops... using list comprehensions... using the zip() function.

```py

# For loops... 
towns = [{'name': 'India', 'population': 58241},
        {'name': 'Chinna', 'population': 12435}, 
        {'name': 'South Sudan', 'population': 25709}]

town_names = []
town_populations =[]

for i in towns:
    town_names.append(i.get('name'))
    town_names.append(i.get('population'))
print(town_names,)

OutPut:
['India', 58241, 'Chinna', 12435, 'South Sudan', 25709]

# List comprehensions... 

town_names = [i.get('name') for i in towns]
town_populations =[i.get('population') for i in towns]
print(town_names,town_populations)

OutPut:
['India', 'Chinna', 'South Sudan'] [58241, 12435, 25709]


# Zip function... 

town_names,town_populations = zip(*[(i.get('name'),i.get('population'))for i in towns])
print(town_names,town_populations)

OutPut:
('India', 'Chinna', 'South Sudan') (58241, 12435, 25709)

```

### 47.Given the two lists (names and populations), combine them back into a list of dictionaries using for loops... using list comprehensions.

```py

names = ["Andhra Pradesh","Telanganna","Karanaka","Keralam"]
populations = [8912345,98989,798493,8498594,789898]

# for loop...

names_populations = []

for index,name in enumerate(names):
    town ={"name":name,"poplutions":populations[index]}
    names_populations.append(town)
print(names_populations)

OutPut:

[{'name': 'Andhra Pradesh', 'poplutions': 8912345}, {'name': 'Telanganna', 'poplutions': 98989}, {'name': 'Karanaka', 'poplutions': 798493}, {'name': 'Keralam', 'poplutions': 8498594}]

# List comprehensions... 
towns = [{ 
    'name': town_name, 
    'population': populations[index] 
} for index, town_name in enumerate(names)] 
print(towns)

OutPut:

[{'name': 'Andhra Pradesh', 'population': 8912345}, {'name': 'Telanganna', 'population': 98989}, {'name': 'Karanaka', 'population': 798493}, {'name': 'Keralam', 'population': 8498594}]

```

### 48.Using the list of towns, find the total combined population using for loops...using the sum() function... using the reduce() function.

```py

from functools import reduce


towns = [{'name': 'Manchester', 'population': 58241}, 
        {'name': 'Coventry', 'population': 12435}, 
        {'name': 'South Windsor', 'population': 25709}]

# For loops... 

total_populations = 0
for i in towns:
    total_populations += i.get('population')

print(total_populations)

OutPut:
96385

# Sum function...

total_populations =  sum(i.get('population') for i in towns)
print("Total Populations Of Countries: ",total_populations)

OutPut:
Total Populations Of Countries:  96385

# Reduce function... 
total_population = reduce(lambda total, town: total + town.get('population'), towns, 0)
print(total_population)

OutPut:
96385

```


------------------------------------------------------------------



