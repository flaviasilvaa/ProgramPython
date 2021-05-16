##This program is going to check how many time in a sentencee the letter 'A' shows and the first and last time that appears
sentence = str(input("Type a sentence\n")).strip().upper()
print('The letter A appears {} times in your sentence'.format(sentence.count('A')))
print('The first the letter A appear is on {} position'.format(sentence.find('A')+1))##because my position starts in 0
print('The last time the letter A appear is on {} position'.format(sentence.rfind('A')+1)) #I am asking to find from the right find
