#this program is going to read 4 values typed by the user and check if there is any number 9, the position of number 3
##and if there is any even number


number = (int(input('Enter first number?\n')),##the () in front my int means is a compost variable
          int(input('Enter second number?\n')),
          int(input('Enter third number?\n')),
          int(input('Enter forth number?\n')))

print('-'*30)
print(f'the numbers typed are {number}')
print('-'*30)
print(f'the number of 9 typed is {number.count(9)} times')
print('-'*30)
if 3 in number:
    print(f'The position of the number 3 typed is {number.index(3)}')
else:
    print('The value 3 was not found it')
print('-'*30)
print(f'The quantity of even numbers is', end= ' ')
for n in number:
    if n % 2 == 0:
        print(n, end= ' ')
