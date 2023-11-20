# How to convert a byte array to String? 

"""
UTF-8--->It stands for "Unicode Transformation Format - 8-bit" 
and is a variable-width encoding that can represent every character in the Unicode character set using one to four bytes.

"""


input_byte = b'Hello, This is input Array'

result = input_byte.decode('utf-8')

print(result)










