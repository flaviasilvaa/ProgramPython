##this program allow to input some arguments to the function

def another_Introduction(name, city):
    print("hello my name is", name)
    print("I live in ", city)

another_Introduction("Maria", "Cork")

another_Introduction("Almir", "Paris")

def num_time(string, times):
    for i in range(times):
        print(string)

num_time("I love Python", 3)

def number(a, b):
    if a > b :
        print("higher number is", a)
    else:
        print("Higher number is ", b)

number(67, 90)

