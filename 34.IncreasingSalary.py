wages = float(input("Inform you wages?\n"))
if wages <= 1250:
    increase = wages * 0.15
    final_wage = wages + increase
else:
    increase = wages * 0.10
    final_wage = wages + increase

print(f'Your new wages is {final_wage}')
