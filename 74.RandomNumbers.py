##this program is going to generate 5 random numbers and store in a tuple, and then is going to show the smallest and the biggest number on the tuple

from random import randint

number = (randint(0, 20)), (randint(0, 20)), (randint(0, 20)), \
         (randint(0, 20)), (randint(0, 20))##when I use a randint inside() I changed from simple variable to compost variable
print(f'the generated numbers is ', end= ' ')
for n in number:
    print(f'{n}', end= ' ')
print(f'\nThe biggest number generated is {max(number)}')
print(f'the smallest number generated is {min(number)}')