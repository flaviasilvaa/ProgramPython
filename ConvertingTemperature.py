#####this program is going to get a temperature in Celsius and convert to Fahrenheit
print("""
.-.                                         .-.           
.' `.                                       .' `.          
`. .'.--. .--. ,-.,-.,-. .--. ,-.,-.,-. .--.`. .'.--. .--. 
 : :' '_.': ..': ,. ,. :' .; :: ,. ,. :' '_.': :' '_.': ..'
 :_;`.__.':_;  :_;:_;:_;`.__.':_;:_;:_;`.__.':_;`.__.':_;  
                                                      """)
temperature = float(input("Inform the temperature in Celsius\n"))
fahrenheit = 9 * temperature / 5 + 32 # in this case if I have parentheses or not wont change my results, it remains the same
print(f'The temperature {temperature}C is {fahrenheit} in fahrenheit')
print('-=-'*30)