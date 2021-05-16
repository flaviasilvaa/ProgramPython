##this program is going to read a real number, a float value and is going to show just the whole number

import math
number = float(input("Type a value\n"))
print(f'the value is {number} and the whole portion is {math.trunc(number)}')# the function trunc is going to count the whole part of a number


##################another option###########################
number = float(input("Type a value\n"))
print(f'The number is {number} and the whole part is {int(number)}')