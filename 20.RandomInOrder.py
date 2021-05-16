#this program is going to choose the students order of presentation in class

from random import shuffle
student1 = str(input("First student\n"))
student2 = str(input("second student\n"))
student3 = str(input("Third student\n"))
student4 = str(input("Forth student\n"))
lista = [student1, student2, student3, student4]
shuffle(lista)
print(f'The presentation order is {lista}')
