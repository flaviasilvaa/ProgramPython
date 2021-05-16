#this program is going to create a multiple table

total = 0 ## this is an accumulator
number = int(input('enter the number to be multiplied?\n'))

for cont in range(1, 11):
    total = number * cont
    print(f' {number} x {cont} = {total}')

###another way ####

number = int(input('Enter the number to be multiplied?\n'))
for cont in range(1, 11):
    print(f'{number} x {cont} = {number * cont}')