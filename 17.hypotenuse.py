####this program is going to calculate the hypotenuse the formule is a2+ b2 =c2###
##where a= side of a right triangle, b= side  of a right triangle and c= hypotenuse, we are going to calculate the lenght

a_opossite = float(input("Type the size of an opposite side of a triangle?\n"))
b_adjacent = float(input("Type the size of an adjacent side of a triangle?\n"))
hypotenuse = (a_opossite ** 2 + b_adjacent ** 2) ** (1/2) ##(1/2) to calculate the square root
print(f'The hypotenuse size is {hypotenuse:.3f}')

###################there is another way to solve it ############################
import math
a_opossite = float(input("Type the size of an opposite side of a triangle?\n"))
b_adjacent = float(input("Type the size of an adjacent side of a triangle?\n"))
hypotenuse = math.hypot(a_opossite, b_adjacent)# this function calculates the hypotenuse just add the a and b variables
print(f"The size of the hypotenuse is {hypotenuse:.2f}")
