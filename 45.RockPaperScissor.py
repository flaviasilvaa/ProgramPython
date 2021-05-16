#this program is going to guess which option the computer choose and check who win the game
from random import randint
from time import sleep
item = ('Rock', 'Paper', 'Scissor')
computer = randint(0, 2)
print("""Your options:
[0]Rock
[1]Paper
[2]Scissor""")
play = int(input("Select your option?\n"))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
print('-='*11)
print(f'Computer selected {item[computer]}')
print(f'You selected {item[play]} ')
print('-='*11)
if computer == 0: #computer choose rock
    if play == 0:
        print('Draw')
    elif play == 1:
        print('You Win :)')
    elif play == 2:
        print('Computer win')
    else:
        print('Wrong option')
elif computer == 1: #computer choose paper
    if play == 0:
        print('Computer win')
    elif play == 1:
        print('Draw')
    elif play == 2:
        print('You Win')
    else:
        print('Wrong option')

elif computer == 2: #computer choose scissor
    if play == 0:
        print('You Win')
    elif play == 1:
        print('Computer win')
    elif play == 2:
        print('Draw')
    else:
        print('Wrong option')


