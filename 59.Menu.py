##this program is going to read two values and them ask what kind of operation the user want to do it (sum, multiplication, greater, new numbers or exit
from time import sleep
total = 0
number1 = int(input('Inform the first number?\n'))
number2 = int(input('Inform the second number\n'))
option = 0
while option != 5:
    print("""
[1]Sum
[2]Multiplication
[3]Greater
[4]New Numbers
[5]Exit
""")
    option = int(input('Choose your option?\n'))
    if option == 1:
        sum = number1 + number2
        print(f'The sum between {number1} and {number2} = {sum}')
    elif option == 2:
        mult = number1 * number2
        print(f'The multiplication between {number1} and {number2} is = {mult}')
    elif option == 3:
        if number1 > number2:
            biggest = number1
        else:
            biggest = number2
            print(f'Between {number1} and {number2} the biggest one is {biggest}')
    elif option == 4:
        print('Inform your numbers agains\n')
        number1 = int(input('Enter first number\n'))
        number2 = int(input('Enter second number\n'))
    elif option == 5:
        print('Finishing.....')

    else:
        print('Wrong option :(')
    print('-=-'*10)
    sleep(1)
print('End of the program')
