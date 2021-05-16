##This program is going to read an angle and will show the sine, cosine and tangent
import math
angle = float(input("Type the angle of a triangle?\n"))
sine = math.sin(math.radians(angle))
print(f"Angle {angle} have a Sine of {sine:.3f}")
cosine = math.cos(math.radians(angle))
print(f"The angle of {angle} have a cosine of {cosine:.2f}")
tangent = math.tan(math.radians(angle))
print(f"The angle of {angle} have a tangent of {tangent:.2f}")