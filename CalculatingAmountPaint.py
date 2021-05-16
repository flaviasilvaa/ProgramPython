##this program is going to get the wall information such height and width to calculate the amount of paint needed to paint the wall
print("""
           ___
       ,--[___]--,
      /           \
     |,.--'```'--.,|    
     |'-.,_____,.-'|    
     |'-.,_____,.-'|    
     |             |   
     |  P A I N T  |  
     |             |  
     |'-.,_____,.-'|  
     `'-.,_____,.-''  
""")

width = float(input("insert the width of the wall?\n"))
height = float(input("insert the height of the wall?\n"))
area = width * height
print('Your wall have a size of {} x {} the total area is {}m2'.format(width, height, area))
paint = area / 2
print('To paint that wall you need {:.3f}liters of paint'.format(paint))