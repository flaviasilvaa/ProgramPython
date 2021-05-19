##this program is going to read gender and age from how many time the users want it to insert asking if they want to enter another data, in the end will show
##how many people are over 18, how many are male and how many are female under 20


total_age = total_male = total_woman = 0
while True:
    age = int(input('Enter age?\n'))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Enter gender [M/F]?\n')).strip().upper()[0]
    if age >= 18:
        total_age += 1
    if gender == 'M':
        total_male += 1
    if gender == 'F' and age < 20:
        total_woman += 1
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Do you want to insert another data[Y/N]?\n')).strip().upper()[0]
    if answer == 'N':
        break
print(f'the total of people over 18 years old is {total_age}')
print(f'The total of registered is {total_male}')
print(f'The total of woman under 20 is {total_woman}')

