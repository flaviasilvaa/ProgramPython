##this program is going to check if is time to the user enlist ##
from datetime import date

actual = date.today().year
year = int(input("inform your birth year?\n"))
age = actual - year
print(f'who born in {year} have {age} in {actual}')
if age == 18:
    print('You should enlist immediately')
elif age < 18:
    many_years = 18 - age
    print(f'You have {many_years} years to enlist')
    year = actual - many_years
    print(f'Your enlist is going to be in {year}')
elif age > 18:
    many_years = age - 18
    print(f'you suppose to enlist {many_years} years ago')
    year = actual - many_years
    print(f'Your enlist was in {year}')
