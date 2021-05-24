###this program is going to read a number is count the number in full 0 to 20, the user should choose one number and that number will be show in full

count = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
         'twenty')

while True:
    while True:
        number = int(input('Choose a number between 0 and 20?\n'))
        if 0 <= number <= 20:
            break
        print(f'Wrong option, try it again', end=' ')
    print(f'You entered the number {count[number]}')
   # answer = ' '
    #while answer not in 'YN':
    answer = str(input('Do you want to check another number [Y/N]?\n')).strip().upper()[0]
    if answer == 'N':
        break
print('='*30, 'End')
