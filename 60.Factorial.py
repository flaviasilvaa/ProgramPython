# this program is going to read a number and show the factorial

from math import factorial

number = int(input('Enter a number to be factored?\n'))
f = factorial(number)
print(f'The factorial of {number}! is {f}')



###another way####
number = int(input('Enter a number to be factored?\n'))
count = number
f = 1
print(f'Calculating {number} ! =', end= ' ')
while count > 0:
    print(f'{count}', end= ' ')
    print('x' if count > 1 else ' = ', end= '')
    f *= count
    count -= 1
print(f'{f}')
