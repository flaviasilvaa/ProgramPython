##this example is going to show how to pass an argument in a function
# by reference in a dictionary, that means my global variable is going to change the values as well

car_speeds = {
    "Golf": 220,
    "Cayenne": 250,
    "Panda": 180,
    "Cooper": 150
}
def change_car_speeds(car_speeds):
    car_speeds["Ferrari"] = 240
    print("Inside the function", car_speeds)

change_car_speeds(car_speeds)

print(car_speeds) #when I call the global variable the change is reflected, the changes reflects everywhere