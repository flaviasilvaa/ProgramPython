##this program is going to calculate the arithmetic progression, showing in the end 10 first terms of this AP using while

first = int(input('First term\n'))
difference = int(input('Common difference\n'))
term = first
count = 1
while count <= 10:
    print(f'{term} ->', end= ' ')
    term += difference
    count += 1
print('End')