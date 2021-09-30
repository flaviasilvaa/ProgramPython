##this project a loop which iterates over a given random list of numbers and prints them
##except if they are divisible by 7
## stops when 315 is encountered



number = [14, 148, 124, 173, 231, 256, 301, 315, 361, 399 ]

for i in number:
    if i == 315:
        break
    if i % 7 == 0:
        continue
    print(i, end =' ')

