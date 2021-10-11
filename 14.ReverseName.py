## this program is going to ask a user to type a name and a last name then reverse it

###The first way to reverse name
name = str(input('inform your first name and last name?\n'))

name_reverse = name.split(" ")
for rev in name_reverse:
    last_index = len(rev) - 1
    for index in range(last_index, -1, -1):
        print(rev[index], end='')
    print(end=' ')
print(end='\n')


###The second way to reverse names
name = input('inform your first name and last name?\n')
first, last = name.split()
print(first[::-1], last[::-1])