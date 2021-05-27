###this  program is going to analyse few words searching for consonants
from time import sleep
print("""
                                                                                                           
   .-.-. .-.-.      .-.-. .-.-. .-.-. .-.-. .-.-. .-.-. .-.-. .-.-. .-.-.      .-.-. .-.-. .-.-. .-.-. .-.-. 
( M .'( y .'.-.-.( f .'( a .'( v .'( o .'( u .'( r .'( i .'( t .'( e .'.-.-.( w .'( o .'( r .'( d .'( s .' 
 `.(   `.(  '._.' `.(   `.(   `.(   `.(   `.(   `.(   `.(   `.(   `.(  '._.' `.(   `.(   `.(   `.(   `.(                                                                                           
                       
""")
sleep(1)
words = ('Python', 'Programmer', 'Experience', 'Opportunity', 'Information',
         'Technology', 'Practicing', 'Learning', 'Developing', 'Studying', 'Knowledge')
for w in words:
    print(f'\nThe word {w.upper()} have', end= ' ')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end= ' ')