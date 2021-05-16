#this program is going to calculate the body mass index.
weight = float(input('Enter your weight in Kilograms[KG]?\n'))
height = float(input('Enter your height in centimeters[CM]?\n'))
BMI = weight/ (height ** 2)# or could be like this(height * height)
print(f'Your BMI is {BMI:.2f}', end=' ')
if BMI <= 18.5:
    print('You are underweight')
elif 18.5 <= BMI < 25:
    print('Normal weight')
elif 25 <= BMI < 30:
    print('Overweight')
elif 30 <= BMI < 40:
    print('Obese')
else:
    print('Morbid obesity')




