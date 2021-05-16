#this program is going to check the car speed if it is over 80 km a car should by a fine calculate by exceeded km per hour
#over 80 km the fine is 7 euros per kilometer exceeded
print(""" 
,---.                   |
`---.,---.,---.,---.,---|
    ||   ||---'|---'|   |
`---'|---'`---'`---'`---'
     |          
""")
speed = float(input("Inform your speed in KM?\n"))

if speed > 80:
    kilometer = (speed - 80) * 7
    print(f"You are over speed, you being fine in {kilometer:.3f} Euros")#simple condition I do not need the else
    #else: can do either way
print("Have a save trip")
