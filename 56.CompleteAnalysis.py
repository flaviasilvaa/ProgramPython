##this program is going to read name, gender and age of 4 people and in the end will show the name of the oldest male and how many women are under 20

total_age = 0
media = 0
media_age = 0
old_man = 0
name_man = ' '
for people in range(1, 5):
    name = str(input(f'Enter {people} person name?\n')).strip()
    age = int(input(f'Enter {people} person age?\n'))
    gender = str(input(f'Enter {people} person gender [M/F]?\n')).strip()
    media += age
    if people == 1 and gender in 'Mm':
        old_man = age
        name_man = name
    if gender in 'Mm' and age > old_man:
        old_man = age
        name_man = name
    if age < 20 and gender in 'Ff':
        total_age += 1
media_age = media / 4
print(f'The average age in the group is {media_age}')
print(f'The oldest man in the group has {old_man} and his name is {name_man}')
print(f'The amount of women under 20 is {total_age}')



