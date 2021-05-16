###this program is going to read 6 numbers if show the sum only of those who are even. If the value entered is odd, disregard it.

total = 0
sum = 0
for count in range(1, 7):
    number = int(input(f'Enter the {count} value?\n'))
    if number % 2 == 0:
        sum = sum + number
        total = total + 1
print(f'You typed {total} Even numbers and the sum of them are {sum}')