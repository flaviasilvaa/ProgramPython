##this program is going to countydown from 10 to 0
from time import sleep

for count in range(10, -1, -1): #-1 is the iteration from the back to the front, and 10 to -1 because I want to count from 10 to 0
    print(count)
    sleep(1)
print('End')
