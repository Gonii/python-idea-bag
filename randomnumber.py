#Guess the  random number
import random
def game():
    print "Can you guess the number ?"
    randomNumber = random.randint(0,100)
    found = False
    while not found:
        answer = int(raw_input(">"))
        if answer == randomNumber:
            print "You got it !"
            found = True
        else:
            if answer > randomNumber:
                print "Guess lower"
            else:
                    print "Guess higher"
game()
