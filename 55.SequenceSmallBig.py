# this program is going to read five people weight in the end will tell who is the lightest one and the heaviest one
light = heavy = 0
for person in range(1, 6):
    weight = float(input(f'Enter {person} weight?\n'))
    if person == 1:  # that means is the first person
        heavy = weight
        light = weight  ##because I did not have any occurrence before
    else:  ##if is not the first person is going to check the conditions
        if weight > heavy:
            heavy = weight
        if weight < light:
            light = weight

print(f"The heaviest weight read is {heavy} Kg and the lightest weight read is {light} Kg")
