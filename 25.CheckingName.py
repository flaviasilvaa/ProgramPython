###this program is going to read the user name and check if they have 'Murphy' in their name
name = str(input("type your full name?\n")).strip()
print('Is your name have Murphy {}'.format('MURPHY' in name.upper()))
