##this program is going to extract some information inserted by the user such as the amount values typed in desc order and if the number 5 is on the list or not

listnumbers = []
total = 0

while True:
    number = int(input('Type a number?\n'))
    answer = str(input('Do you want to continue?[Y/N]\n')).strip().upper()[0]
    if answer in 'Yy':
        total += 1
    else:
        break
print('-='*30)
print(f'The amount of numbers typed are {total}')