#this program is going to calculate the new salary increased in 15%
print("""
_ __ ___   ___  _ __   ___ _   _ 
| '_ ` _ \ / _ \| '_ \ / _ \ | | |
| | | | | | (_) | | | |  __/ |_| |
|_| |_| |_|\___/|_| |_|\___|\__, |
                             __/ |
                            |___/ 
""")
salary = float(input("Type your salary\n"))
increase = salary + (salary * 15 / 100)
print(f'Your salary is {salary} Euros and after increase 15% is {increase} Euros')