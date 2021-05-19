###this program is going to read numbers informed by the user and them is going to show in the end the quantity of numbers inserted and the average between them
answer = 'Y'
total = add = average = 0
while answer in 'Y/y':
    number = int(input('Type a number?\n'))
    add += number
    total += 1
    answer = str(input('Do you want to continue?[Y/N]\n')).strip().upper()[0]
average = add / total
print(f'You inserted  {total} numbers and the average between them is {average}')
