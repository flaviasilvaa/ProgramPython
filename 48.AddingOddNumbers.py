##this program is going to calculate the sum between all numbers that are multiples of three and that are in the range of 1 to 500

total = 0 #this variable starts in zero and then is going to receive the numbers from numbers, this is an accumulator
cont = 0 ##this is a counter, is going to store how many times something happened
for number in range(1, 501, 2):
    if number % 3 == 0:
        total += number
        cont = cont + 1
print(f'the amount of odd numbers is {cont} and the sum between all odd numbers is {total}')