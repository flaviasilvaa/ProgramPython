#this program is going to ask to the user to insert 3 numbers and is going to check with one is the biggest one and the smallest one
number1 = int(input("Inform the first number?\n"))
number2 = int(input("Inform the second number?\n"))
number3 = int(input("Inform the third number?\n"))
smallest = number1
if number2 < number1 and number2 < number3:
    smallest = number2
if number3 < number1 and number3 < number2:
    smallest = number3
print(f'The smallest number is {smallest}')
biggest = number1
if number2 > number1 and number2 > number3:
    biggest = number2
if number3 > number1 and number3 > number2:
    biggest = number3
print(f'The biggest number is {biggest}')