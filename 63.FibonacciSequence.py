##this program is going to read a number and show the fibonacci sequence that means we need to sum the 2 previous terms to get the next term

print('-'*30)
print("Fibonacci Sequence")
print('-'*30)
number = int(input("How many terms do you want to show?\n"))
t1 = 0 #this is default
t2 = 1 #this is default
###t1 and t2 are default because they will be in ever single fibonacci sequence does not matter the quantity of terms
print('-'*30)
print(f'{t1} -> {t2}', end= '')
count = 3 ##my counter is going to start in 3 because I do have my 3 default values
while count <= number:
    t3 = t1 + t2
    print(f' -> {t3}', end= ' ')
    t1 = t2 ##t1 is going to be t2 and t2 is going to be t3 when starts to execute my while
    t2 = t3
    count += 1
print(f'-> End')
