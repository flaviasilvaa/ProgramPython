##this program is going to ask the user to insert a number and is going to multiple by 3 until type 'out'

while True:
    value = input("Type a number\n")

    if value == "out":
        print("Good bye!!!") ##break statement is going to be executed
        break

    if not value.isdigit(): # if input is not a digit move on to the next iteration
        print("Enter another number\n")
        continue

    value = int(value)
    print("Cube of %d is %d" %(value, value ** 3))
