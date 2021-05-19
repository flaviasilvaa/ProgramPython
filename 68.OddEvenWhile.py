##this program the computer is going to play with the user, the user should pick a number and choose if even and odd and the game is over when the user lose

from random import randint
win = 0
while True:
    number = int(input('Enter a number?\n'))
    computer = randint(0, 11)
    total = number + computer
    choice = ' '
    while choice not in 'EO':
        choice = str(input('Even or Odd?[E/O]?\n')).strip().upper()[0]
    print(f'Your typed {number} and computer choose {computer} the total of {total}')
    print('It is Even' if total % 2 == 0 else 'It is Odd')
    if choice == 'E':
        if total % 2 == 0:
            print('You win')
            win += 1
        else:
            print('You won')
            break
    elif choice == 'O':
        if total % 2 == 1:
            print('You win')
            win += 1
        else:
            print('You lose')
    print('Let s play it again!!!!')
print(f'Game over!!! you win {win} times')

