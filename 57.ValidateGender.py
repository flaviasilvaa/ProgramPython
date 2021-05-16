#this program is going to validate a gender if is different of male and female will ask to type a correct information


gender = str(input(f'enter your gender [M/F]?\n')).strip().upper()[0]
while gender not in 'Mm/Ff':
    gender = str(input('Wrong data, please enter your gender\n')).strip().upper()[0]
print(f'Gender {gender} successfully registered')