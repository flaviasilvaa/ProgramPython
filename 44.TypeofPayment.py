##this program is going to calculate the value paid in a product based in the type of payment
print("""Flavia's Store

_        ,
                            (_\______/________
                               \-|-|/|-|-|-|-|/
                                \==/-|-|-|-|-/
                                 \/|-|-|-|,-'
                                  \--|-'''
                                   \_j________
                                   (_)     (_)

""")
value = float(input('Enter the value of the shop?\n'))
print("""Payment options
[1] money/cheque
[2] card
[3] 2x card
[4] 3x or more on the card""")
option = int(input("Type the payment option?\n"))
if option == 1:
    total = value - (value * 10 / 100)
elif option == 2:
    total = value - (value * 5 / 100)
elif option == 3:
    total = value
    instal = total / 2
    print(f'Your shop is going to have 2x of {instal} Euros')
elif option == 4:
    total = value + (value * 20 / 100)
    totintal = int(input('How many instalments?\n'))
    install = total / totintal
    print(f'Your shop is going to have {totintal} x of {install} Euros with fees')
else:
    total = value
    print(f'Wrong option, try it again')
print(f'Your shop {value} Euros is going to cost {total} Euros')


