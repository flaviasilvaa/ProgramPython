##this program is going to read a number from a user input and convert to binary, Octal or Hexadecimal
import math
number = int(input("Type a number?\n"))
print("""Please choose one of the bases for conversion:
[1] Convert to binary
[2] Covert to Octal
[3] Convert to Hexadecimal 
""")
choose = int(input('option number?\n'))
if choose == 1:
    print(f'The number {number} to binary is {bin(number)[2:]}') #the[2:] is going to slice that means the first 2 numbers won't show it
elif choose == 2:
    print(f'The number {number} to octal is {oct(number)[2:] }') #the first 2 numbers would start with 0b or 0o or 0h they are not necessary
elif choose == 3:
    print(f'The number {number} in hexadecimal is {hex(number) [2:]}')# this is a reason I sliced them