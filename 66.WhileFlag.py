###this program is going to read numbers and is going to stop when the user type 999 and in the end is going to show the sum between them

number = add = total = 0
while True:
    number = int(input('Enter a number?[To stop type 999]\n'))
    if number == 999:
        break
    total += 1
    add += number
print(f'sum between {total} numbers is {add}')