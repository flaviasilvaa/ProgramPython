##this program is going to calculate the total due based in the amount of kilometers travelled and the quantity of days rented.
##the price of the rent is 35.00 euros per day plus 0.15 cents per km travelled.
print("""
    _______
   /______/"=,
  [     | "=, "=,,
  [-----+----"=,* )
  (_---_____---_)/
    (O)     (O)""")
kilom = float(input("Inform the amount of kilometers travelled?\n"))
days = int(input("Inform the amount of days rented?\n"))
total = (days * 35) + (kilom * 0.15)
print(f'The amount due is {total} Euros ')
