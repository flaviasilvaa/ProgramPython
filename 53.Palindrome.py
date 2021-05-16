#this program is going to check if a sentence is a plaindrome(reading backward is the same)

sentence = str(input('Enter a sentence to be checked?\n')).strip().upper()
word = sentence.split()# I am going to divide the words in my sentence and them join them, made a list
join = ' '.join(word)##joint the list, everything in a string
inverse = ' '##just reverse them
for letter in range(len(join)-1 , -1, -1):#it is going to back
    inverse += join[letter]
print(f'The inverse of {sentence} is {inverse}')
if inverse == join:
    print(f'This is a palindrome ')
else:
    print(f'The sentence is not a palindrome')


######another way######

sentence = str(input('Enter a sentence to be checked?\n')).strip().upper()
word = sentence.split()# I am going to divide the words in my sentence and them join them, made a list
join = ' '.join(word)##joint the list, everything in a string
inverse = join[::-1]
print(f'The inverse of {sentence} is {inverse}')
if inverse == join:
    print(f'This is a palindrome ')
else:
    print(f'The sentence is not a palindrome')