##this program is going to read the name and the price of many products asking if the user wants to insert more
##in the end will show to total spend, which product cost more than 1000 and the name of the cheapest product
print("""
                            Flavia's Shopping
 _        ,
                            (_\______/________
                               \-|-|/|-|-|-|-|/
                                \==/-|-|-|-|-/
                                 \/|-|-|-|,-'
                                  \--|-'''
                                   \_j________
                                   (_)     (_)
""")

total_price = over_price = count_product = cheap = 0
cheap_name = ' '
while True:
    name = str(input('Enter the name of the product?\n'))
    price = float(input('Enter the price of the product?\n'))
    count_product += 1
    total_price += price
    if price > 1000:
        over_price += 1
    if count_product == 1:## if count_product ==1 or price < cheap and get rid of the else and if statement because the just repeat the same information both blocks are the same
        cheap = price
        cheap_name = name
    else:  ###I could eliminate this block and put it everything in the if statement(just for learning purpose)
        if price < cheap:
            cheap = price
            cheap_name = name
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Do you want to continue[Y/N]\n')).strip().upper()[0]
    if answer == 'N':
        break
print('-'*40, 'End')
print(f'The total purchase is  {total_price}')
print(f'The total  {over_price}  products that costs over a 1000 Euros')
print(f'The cheapest product is {cheap_name} and it costs {cheap:.2f} Euros')