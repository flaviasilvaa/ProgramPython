##this program is going to check for a ticket price based on Km travelled till 200 is going to be charged 0.5 per km and over 200 the price changes for .45

kilometers = float(input("How many kilometers is your journey?\n"))
if kilometers <= 200:
    price = kilometers * 0.50

elif kilometers >= 200:
    price = kilometers * 0.45

print(f'the amount due for your ticket is {price}')
######or we can do in another way as well ######
kilometers = float(input("how many kilometers is your journey?\n"))
price = kilometers * 0.50 if kilometers <= 200 else kilometers * 0.45
print(f'The final price of your journey is {price}')