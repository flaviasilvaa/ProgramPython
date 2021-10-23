##this program is going to create a function using list

def generate_list(name, num_elements):
    return [name for i in range(num_elements)]


some_list = generate_list("flavia", 7)

print(some_list)


###another way####
def generate_list(name, num_elements):
    return_list = []
    for i in range(num_elements):
        return_list.append(name)

        return return_list


some_list = generate_list("Ben", 3)
print(some_list)
