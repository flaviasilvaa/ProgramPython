# this is a guess the number game.
import random

print('Hello, what is your name?')
name = input()  # variable name is going to store the name typed

print('Nice  to meet you' + name + ',I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

#print('DEBUG: secret number is' + str(secretNumber))

for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break  # this condition if for the correct guess

if guess == secretNumber:
    print(f'good job' + name + 'you guessed my number in' + str(guessTaken) + 'guesses')
else:
    print(f'Nope, the number I was thinking of was' + str(secretNumber))
