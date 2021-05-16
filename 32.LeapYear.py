#this program is going to check if the chosen year  is a leap year

year = int(input("Type a year to be checked?\n"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"the year {year} is a leap year")
else:
    print(f'The year {year} is not a leap year')


#####I can check the year from the user machine if it is a leap year

from datetime import date

year1 = int(input("Which year do you want to analyse? if you want the actual date type 0\n"))
if year1 == 0:
    year1 = date.today().year
if year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0:
    print(f'The year {year1} is a leap year')
else:
    print(f'The year {year1} is not a leap year')
