##this program is going to read values and add in a list if the number is already on the list it will not be add in the end the program is going to show the numbers typed in order

numbers = list()

while True:
    number = int(input("Type a number?\n"))
    if number not in numbers:
        numbers.append(number)##to insert the number on the list
        print('Value added successfully')
    else:
        print('Double value, It cannot be added')
    answer = str(input('Do you want to continue?[Y/N]\n')).strip().upper()[0]
    if answer in 'Nn':
        break
print('-='*30)
numbers.sort()##to put the number in order
print(f'You typed these values {numbers}')