##this program is going to show the multiple table of a lot of numbers, the program will stop when the user type a negative number

while True:
    number = int(input('Enter a number to be multiplied?\n'))
    print('-' * 30)
    if number < 0:
        break
    for cont in range(1, 11):
        print(f'{number} x {cont} = {number * cont}')
        print('-'*30)
print('End')
