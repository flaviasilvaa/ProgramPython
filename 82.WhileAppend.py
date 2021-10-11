##this program is going to use a while in a range of 50 and print in a list skipping the number if they are divided by  or 7

my_list = []
num = 0

while num in range(0, 50):

    num += 1
    if num % 5 == 0 or num % 7 == 0:
        continue
    my_list.append(num)
print(my_list)