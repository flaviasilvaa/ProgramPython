##this program is going to count even number from 1 to 50


for number in range(1, 51):
    if number % 2 == 0:
        print(number, end= ' ')##to print everything in the same line


######another option
for number in range(2, 51, 2):#the difference in this one is less iteration to print the number, less execution
    print(number, end= ' ')# less repetition, less use of the machine
