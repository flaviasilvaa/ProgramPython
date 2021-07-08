##this program is going to read 5 numbers in a list and then compare the smallest and the biggest number


listnum = []
small = big = 0

for c in range(0, 5):
    listnum.append(int(input(f"type a number for position {c}\n")))
    if c == 0:
        small = big = listnum[c] ##I don't know which one is the smallest or the biggest
    else:
        if listnum[c] > big: ##checking the biggest value
            big = listnum[c]
        if listnum[c] < small: ##checking for the smallest value
            small = listnum[c]
print('-=' * 30)
print(f'you typed the numbers{listnum}')
print(f'The biggest number is {big} in the position', end=' ')
##I need to swipe my whole list to check the position of the biggest and smallest
for i, v in enumerate(listnum):#I have the indice and value
    if v == big:
        print(f'{i}...', end= ' ')# is going to check the position of the biggest number
print()
print(f' The smallest number is {small} in the position', end=' ')
for i, v in enumerate(listnum): ##I can use the same 'variable' i and v
    if v == small:
        print(f'{i}...', end=' ')
print()


