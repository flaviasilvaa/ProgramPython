##this program is going to register 5 number in a list inserting those number in the position typed

listNumbers = []

for count in range(0, 5):
    number = int(input('Type a value\n'))
    if count == 0 or number > listNumbers[-1]: ##that means is the first one l==0 and the second part if the number is greater than the list is going to add the number less one position
        listNumbers.append(number)
        print('Added to the end of the list')
    else:### I am going to swipe the whole vector, my list
        position = 0 #is going to verify the positions
        while position < len(listNumbers):
            if number <= listNumbers[position]: ## I'm going to check if the number I'm going to enter is equal to or less than it, if is equal or less i will insert it
                listNumbers.insert(position, number)
                print(f'Add in the position {position}')
                break
            position += 1
print('-='*30)
print(f'The values typed are  {listNumbers}')




