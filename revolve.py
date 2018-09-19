# OBJECTIVE: SHOOT TO GAIN 10, PASS AND -5, PASS TWICE IN A ROW -5 TURNS INTO -10
import random
print "~" * len("The revolver has 1 bullet in its chamber")
print """The revolver has 1 bullet in its chamber
You can shoot(+10 points) or pass(-5 points)
Every time you pass, the pass amount is times 2"""
print "~" * len("You can shoot(+10 points) or pass(-5 points")
print "Choose your difficulty by number:\n(1)Zvicerr: 50 points to win\n(2)Medium:100 points to win\n(3)Kosov:200 points to win"
cylinder = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print "Spinning the revolver cylinder..."
cylinder[random.randint(0, 8)] = 1


def game():
    value = 0
    difficulty = int(raw_input(">"))
    if difficulty != 1 or difficulty != 2 or difficulty != 3:
        print "Choose 1,2 or 3"
        game()
    count = 0
    passcount = 1
    for i in cylinder:
        print "ROUND {}".format(int(count) + 1)
        a = raw_input("Shoot ?\n>")
        if a == "yes" or a == "yes".upper() or a == 'y' or a == 'y'.upper():
            if cylinder[count] == 1:
                print "Dead."
                break
            else:
                print "You survived(+10)."
                value += 10
                print "Account:{}".format(value)
        elif a == "no" or "no".upper() or a == "n" or a == "n".upper():
            print "You passed"
            value -= 5 * passcount
            print "Account:{}".format(value)
            passcount += 1
        if difficulty == 1:
            if value >= 50:
                print "You win"
                break
        elif difficulty == 2:
            if value >= 100:
                print "You win"
                break
        else:
            if value >= 200:
                print "You win"
                break
        count += 1


game()
