print("""
                              |              
,---.,---.,---..    ,,---.,---.|--- ,---.,---.
|    |   ||   | \  / |---'|    |    |   ||    
`---'`---'`   '  `'  `---'`    `---'`---'`    

""")
convertor = int(input("Type a number to be converted in meters\n"))
print('-=-' * 30)
decimeter = convertor * 10  # dm
centimeters = convertor * 100  # cm
milimeters = convertor * 1000  # mm

decameter = convertor / 10  # dam
hectometer = convertor / 100  # hm
kilometer = convertor / 1000  # km
print(f'The measures of {convertor} in decimeter is {decimeter}\n in centimeters is {centimeters}\n', end=' ')
print(
    f'in mm is {milimeters}\n in decameters is {decameter}\n in hectometer is {hectometer}\n and in kilometers is {kilometer}')
print('-=' * 30)
