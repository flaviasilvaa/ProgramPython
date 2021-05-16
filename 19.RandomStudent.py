#this program is going to choose one student between 4 of them to do a presentation to the class
import random
student1 = str(input("First student\n"))
student2 = str(input("Second Student\n"))
student3 = str(input("Third Student\n"))
student4 = str(input("Fourth student\n"))
lista = [student1, student2, student3, student4]
chosen = random.choice(lista)
print(f'The student chosen to start the presentation is {chosen}')

