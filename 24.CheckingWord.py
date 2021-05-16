###this program is going to read the name of a city and check if there is any 'New' in that word

city = str(input("type the name of the city\n")).strip()
print(city[:3].upper() == 'NEW')