##this program is going to read the swimmers by the year and classify the categories
from datetime import date
actual = date.today().year
year = int(input("Enter your year of birth?\n"))
age = actual - year
print(f'The athlete have {age} years')
if age <= 9:
    print(f'Your category is Little')
elif age <= 14:
    print(f'Your category is kids ')
elif age <= 19:
    print(f'Your category is Junior')
elif age <= 25:
    print(f'Your category is Senior')
else:
    print(f'your category is Master')