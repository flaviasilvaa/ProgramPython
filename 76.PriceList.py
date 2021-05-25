##this program is going to show a price list using tuple

school_list = ('Pen', 2,
               'Notebook', 5.45,
               'Book', 15.87,
               'Pencil', 3.23,
               'Ruler', 1,
               'Backpack', 30.43,
               'eraser', .45,
               'Pencil Case', 3.12,)
print('-'*40)
print("""
            _                 _     _  _            
           | |               | |   | |(_)       _   
  ___  ____| |__   ___   ___ | |   | | _  ___ _| |_ 
 /___)/ ___)  _ \ / _ \ / _ \| |   | || |/___|_   _)
|___ ( (___| | | | |_| | |_| | |   | || |___ | | |_ 
(___/ \____)_| |_|\___/ \___/ \_)   \_)_(___/   \__)
""")
print('-'*40)
for position in range(0, len(school_list)):##it is going to go until the size of the list
    if position % 2 == 0: # that means is in the left it is the name of the product
        print(f'{school_list[position]:.<30}', end= ' ')
    else:
        print(f'{school_list[position]:>7.2f} Euros')
print('-'*40)
