##this program is going to make an operation and return using functions

def operation(num1, num2):
    result = num1 - num2
    return result;  """to get information from a function"""

r = operation(23,7)
print(r)



def max_number(a_list):
    element = a_list[0]
    lenght = len(a_list)
    for i in range(1, lenght):
        if a_list[i] > element:
            element = a_list[i]
    return element

num = [2,3,6,87,56]
element = max_number(num) ## is going to find the biggest number on my list
print(element)


def positive_negative_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "zero"


positive_negative_number(-9)
print(positive_negative_number(-9))
print(positive_negative_number(0))