##this program is going to check between 6 people who is under or over 18
from datetime import date
actual = date.today().year
total = total1 = 0

for count in range(1, 8):
    year = int(input(f'Which year the {count} person born?\n'))
    age = actual - year
    if age <= 18:
        total += 1

    else:
        total1 += 1

print(f'the total of under 18 is {total} and the total of over 18 is {total1}')
