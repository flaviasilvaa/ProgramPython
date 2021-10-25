##this is just a sample in how to declare a local variable

country = "Ireland"
city = "Dublin"

def some_fun():
    print("Country:", country)
    print("City:", city)



def some_fun():
    country = "Brazil"

    print("Country:", country)
    print("City:", city)
some_fun() ## is going to print the local variable in this case Brazil