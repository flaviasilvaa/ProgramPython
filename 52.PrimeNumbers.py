# this program is going to check if a number is prime or not(divided by itself and for one)
total = 0
number = int(input('Enter a number to be checked\n'))
for count in range(1, number + 1):
    if number % count == 0:
        print('\033[33m', end=' ')  # end to not skip to the next line
        total += 1
    else:
        print('\033[31m')
    print(f'{count}', end=' ')
print(f'\n\033[m the selected number {number} was divided {total} times', end=' ')
if total == 2:
    print(f'In this case {number} is prime')
else:
    print(f'In this case {number} is not prime')
