###this program is going to read numbers informed by the user and them is going to show in the end the quantity of numbers inserted and the average between them
##and the smallest and the biggest number

answer = 'Y'
quantity = add = average = smallest = biggest = 0
while answer in 'Y/y':
    number = int(input('Type a number?\n'))
    add += number
    quantity += 1
    if quantity == 1:
        biggest = smallest = number
    else:
        if number > biggest:
            biggest = number
        if number < smallest:
            smallest = number
    answer = str(input('Do you want to continue?[Y/N]\n')).strip().upper()[0]
average = add/ quantity
print(f'You inserted  {quantity} numbers and the average between them is {average}')
print(f'The smallest number is {smallest} and the biggest number is {biggest}')
############################################################################

