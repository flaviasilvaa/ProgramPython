##this program is going to ask the user the capital of Cairo while they do not get it
##right or type 'quit' the program will still running
answer = " "

while True:
    answer = str(input("What is the capital of Egypt?\n")).upper()

    if answer == "quit":
        print('The correct answer is Cairo, I am sorry you could not get this time,Good bye!!')
        break

    if answer == 'CAIRO':
        print("That is the correct answer, congrats!!!")

        break

    else:
        print("This is not the right answer, please try it again")
