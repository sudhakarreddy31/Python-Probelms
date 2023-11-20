# Write A Program Palindrom



string = input("Enter A Sting :" ).lower()

if string == string[::-1]:
    print(f"{string} Is Palindrome")
else:
    print(f"{string} Is  Not Palindrome")




# str = 'SUDHAKAR'.lower()

# if str == str[::-1]:
#     print(f"{str} Is Palaindrome..!")
# else:
#     print(f"{str} Is Not Palaindrome..!")



def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


s=is_palindrome("Sudhakar")
print(s)