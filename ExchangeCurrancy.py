##This program is going to ask how much a person wants to exchange from Reais to Euros and Dollar
print("""
  _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ 
( E | x | c | h | a | n | g | e )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
""")
real = float(input("How much do you want to exchange?Reais\n"))
euro = real / 6.96
dollar = real / 6.43
print(f'With {real:.2f} Reais  you can buy {euro:.2f} Euros\nWith {real:.2f}Reais you can buy {dollar:.2f} Dollar')

