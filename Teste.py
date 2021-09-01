a = 19 // 2
b = 19 % 2
x = 'curso de python'
print(f'{a}')
print(f'{b}')

print('vc se chama() e tem ()'.format(a, b))


for c in range (0, 10, 3):
    print(c)

for c in range (0,5):
    print(c)

length = 0
if length :
        print("hello world")


name = str(input('inform your first name and last name?\n'))

name_reverse = name.split(" ")
for rev in name_reverse:
    last_index = len(rev) - 1
    for index in range(last_index, -1, -1):
        print(rev[index], end='')
    print(end= ' ')
print(end= '\n')

name = input('inform your first name and last name?\n')
first, last = name.split()
print(first[::-1], last[::-1])

string = "Hello"
print(string[::-1])
