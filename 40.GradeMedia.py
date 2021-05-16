#this program is going to read 2 input from a student and calculate the media between them and inform if is under 5 is reproved, 5 to 6.9 retest and over 7 aproved
note1 = float(input("inform your first grade?\n"))
note2 = float(input("inform your second grade?\n"))

final = (note1 + note2) / 2
if final <= 5:
    print(f'Your final result is {final} and you did not pass :(')
elif final <= 6.9:
    print(f'your final result is {final} and you need do to the test again!!!')
else:
    print(f'your final result is {final} Congratulations you pass it')
print(f'your final result is {final}')