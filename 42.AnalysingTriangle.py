#this program is going to analyse triangles if it is a equilateral(all the sides are equal) isosceles( 2 sides are equal and one is diferrent
##or if a triangle is scalene(all the sides are different)
segment1 = float(input('Enter the first segment?\n'))
segment2 = float(input('Enter the second segment?\n'))
segment3 = float(input('Enter the third segment?\n'))
if segment1 < segment2 + segment3 and segment2 < segment1 + segment3 and segment3 < segment1 + segment2:
    print(f"the segments can form a triangle", end= ' ')
    if segment1 == segment2 and segment2 == segment3:  ##nested conditions
        print('Equilateral ')
    elif segment1 != segment2 != segment3 != segment1:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print(f'The segments cannot form a triangle')