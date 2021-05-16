##This is a simple program that is going to ?read two students note and calculate their average score
#import emoji
#print(emoji.emojize("hello world  :cat:", use_aliases=True)) # need to say a string first and then the name of the emoji

note1 = float(input("type the first student grade?\n"))
note2 = float(input("type the second student grade?\n"))
total = (note1 + note2) / 2
print('The average score between {:.1f} and {:.1f} is {:.1f}'.format(note1, note2, total))