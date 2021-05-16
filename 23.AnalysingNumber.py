##this program is going to slice a number using just math
##modulo or mod is the remainder after dividing one number by another
number = int(input("Type a number[from 0 to 9999]?\n"))
unit = number // 1 % 10 #is going to be a number dividide by 1 module of 10
dozens = number // 10 % 10 # the same logic the number dividide by 10 module of 10
hundred = number // 100 % 10# module is the rest of the division
thousand = number // 1000 % 10
print(f'Analysing the number{number}')
print(f'Unit {unit}')
print(f'Dozens {dozens}')
print(f'Hundred {hundred}')
print(f'Thousand {thousand}')