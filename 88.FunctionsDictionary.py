##this program is going to create a function using dictionary

def create_dictionary(name, age, occupation):
    dictionary = {
        "name": name,
        "age": age,
        "occupation": occupation
    }
    return dictionary


info_dictionary = create_dictionary("Ben", 46, "Software Tester")
print(info_dictionary)

info_dictionary = create_dictionary("Flavia", 41, "Software Developer")
print(info_dictionary)