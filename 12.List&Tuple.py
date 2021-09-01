##this program is going to split numbers(in a string)and make them to be list and tuples

values = input("enter some comma separated numbers :")

list_value = values.split(",")
tuple_value = tuple(list_value)

print("List : ", list_value)
print("Tuple : ", tuple_value)

