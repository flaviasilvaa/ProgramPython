##this program is going to get a set of random number if they are divided by 3 nothing happens
##it will no show, otherwise the x number is going to exxponentated by 3

number_list = [2, 3, 6, 9, 78, 6, 13, 56, 87, 10, 12]

cube_list = [x ** 3 for x in number_list if x % 3 == 0]

print(cube_list)