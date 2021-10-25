##this program is going to get some data from a function in dictionary

def student_details(**details):
    if 'name' in details:
        print("Name:", details['name'])

    if 'age' in details:
        print("Age:", details['age'])

    if 'college' in details:
        print("College", details['college'])

##Need to pass the arguments to be printed
student_details(name = "Flavia")
student_details(name="Peter")
student_details(age=41, college="CCT")


