#this program is going to analyse the user name, showing the first and the last name
name = str(input("Type your full name?\n")).strip()
total_name = name.split()#split is going to slice the name in divide by spaces and is going to put in a list
print('Nice to meet you')
print('Your first name is {}'.format(total_name[0]))
print('Your last name is {}'.format(total_name[len(total_name)-1]))
