##this program the computer is going to think in one number and the user will try to guess the number in the end will show how many times the user tried to guess

from random import randint
total = 0
computer = randint(0, 10)
print('-=-' * 30)
guess = int(input('Try to guess a number from 0 to 10?\n'))
print('-=-' * 30)
while computer != guess:
    guess = int(input('Try it again your guess is wrong\n'))
    total += 1
    if computer == guess:
        print(f'congratulations the computer chose {computer} and you bet the machine after {total} times ')

#####Another way ######
from random import randint
total_guess = 0
guess = False
computer = randint(0, 10)
print('-=-' * 30)
print('Try to guess a number from 0 to 10?')
while not guess:
    player = int(input('Your guess\n'))
    total_guess += 1
    if player == computer:
        guess = True
    else:
        if player < computer:
            print('Higher number.. Try it again!!!')
        elif player > computer:
            print('Lower number...Try it again!!!')
print(f'You guessed in {total_guess} times.Congrats!!!')


