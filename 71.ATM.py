###this program is going to simulate an ATM reading the amount requested and the notes should be 50, 20 , 10 and 5

print("""
 ______                    __       
|_   _ \                  [  |  _   
  | |_) |  ,--.   _ .--.   | | / ]  
  |  __'. `'_\ : [ `.-. |  | '' <   
 _| |__) |// | |, | | | |  | |`\ \  
|_______/ \'-;__/[___||__][__|  \_] 
""")
print('='*30)
value = int(input('Enter the amount to withdraw?\n'))
total = value
notes = 50 ###starts with the biggest one
total_notes = 0
while True:
    if total >= notes: ##if I can subtract
        total -= notes ##I am going to try subtracting 50 from this amount
        total_notes += 1 # everytime I take 50 my total notes get + 1
    else:
        if total_notes > 0:
            print(f'Total of notes {total_notes} of {notes} Euros')
            print('=' * 30)
            print('See you soon!!!!!')
        if notes == 50: ##if I cannot take 50 my next note is equal 20
            notes = 20
        elif notes == 20:
            notes = 10
        elif notes == 10:
            notes = 5
        total_notes = 0
        if notes == 0:
            break


