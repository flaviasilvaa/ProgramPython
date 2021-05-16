##this program is going to calculate the arithmetic progression, showing in the end 10 first terms of this AP

first_term = int(input('first term\n'))
difference = int(input('Common difference\n'))
decimal = first_term + (10 - 1) * difference
for count in range(first_term, decimal + difference, difference):
    print(f'{count}', end= ' ->')
print('End')