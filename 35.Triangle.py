##this program is going to check if with the size of the line I can form a triangle
r1 = float(input("first segment\n"))
r2 = float(input("Second segment\n"))
r3 = float(input("Third segment\n"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(f'The segments above can form a triangle ')
else:
    print(f'The segment above cannot form a triangle')


19//2