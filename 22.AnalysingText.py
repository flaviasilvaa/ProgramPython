#this program is going to ask a user to type their full name and the program is going to show the name in upper case and lower case
#how many letters in their name and how many letters the user have in their first name
name = str(input("Type insert your name?\n")).strip()
print('-=-'*30,'Analysing your name')
print(f'Your name in upper case is {name.upper()}')
print(f'Your name in lower case is {name.lower()}')
print('The amount of letter in yor name is {}'.format(len(name) - name.count(' ')))#minus the space counting
print(f"Your first name have {name.find(' ')} letters")
#####another way to check the first name######
separate = name.split()
print(f'Your first name is {separate[0]} and your name has {len(separate[0])} letters')
