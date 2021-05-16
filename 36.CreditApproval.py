##this program is going to approve or deny the user credit to buy a house, to approve cannot compromise more than 30% of the customer salary
house = float(input("Inform the house price?\n"))
salary = float(input("What is your salary monthly?\n"))
years = int(input("How may year would like to pay the mortgage?\n"))

installments = house / (years * 12)
mortgage = salary * 30 / 100
print(f'Buying a house of {house:.2f}euros in {years}', end=' ')
print('The installments is going to be {:.2f} Euros per month'.format(installments))
if installments <= mortgage:
    print("You mortgage can be approved")
else:
    print("Unfortunately you do not have enough funds for these mortgage")
