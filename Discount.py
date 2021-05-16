print("""
88888b.d88b.  .d88b. 88888b.  .d88b. 888  888 
888 "888 "88bd88""88b888 "88bd8P  Y8b888  888 
888  888  888888  888888  88888888888888  888 
888  888  888Y88..88P888  888Y8b.    Y88b 888 
888  888  888 "Y88P" 888  888 "Y8888  "Y88888 
                                          888 
                                     Y8b d88P 
                                      "Y88P" 
""")
price = float(input("insert the price of the product:\n"))
discount = price - (price * 5 / 100)
print(f'The product cost {price:.2f} Euros and the final price with a discount is {discount:.2f} Euros')