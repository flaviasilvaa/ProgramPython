#this program the computer is going to 'think' in one number and the user is going to try to guess the number the computer chosen
from time import sleep
from random import randint
computer = randint(0, 5)
print('-=-'*30)
guess = int(input("Try to guess the computer number[from 0 to 5]?\n"))
print('-=-'*30)
print('thinking......')
sleep(1)
if computer == guess:
    print(f"Congrats you bet the computer")
else:
    print(f'you are wrong my number is {computer} and your guess is {guess}')

