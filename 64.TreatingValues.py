###this program is going to read whole numbers from the users and just will stop when the user type 999 in the end will show how many numbers was typed and the sum between them

number = count = final = 0
number = int(input('Type a number[999 to stop]?\n')) ##if I put this command 2 that means my flag 999 will not be consider or add in my sum, won't be calculated
while number != 999:
    final += number
    count += 1
    number = int(input('Type a number[999 to stop]?\n'))
print(f' You Typed {count} numbers and the total between them is {final}')
