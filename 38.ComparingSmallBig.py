##this program is going to read the user input, 2 numbers and check with one is the smallest, the biggest or just a draw
number1 = int(input("type a number?\n"))
number2 = int(input("type another number?\n"))
if number1 > number2:
    print(f'The number first number is the biggest')
elif number2 > number1:
    print(f'The second number is the biggest one')
elif number1 == number2:
    print(f'Both values are the same')
