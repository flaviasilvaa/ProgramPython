##this program is going to calculate the arithmetic progression, showing in the end 10 first terms of this AP using while
##in this one is going to ask if the user wants to insert more terms after read the 10 first term

first = int(input('First term\n'))
difference = int(input('Common difference\n'))
term = first
count = 1
total = 0
more_terms = 10  # starts to insert more terms after show the 10 first
while more_terms != 0:
    total = total + more_terms
    while count <= total:
        print(f'{term} ->', end=' ')
        term += difference
        count += 1
    print('Pause')
    more_terms = int(input('How many more terms do you want to show it?\n'))
print(f'The arithmetic progression was finished with {total} terms')
