import random
n = int(raw_input("How many times do you want to coin flip?\n>"))


def flipcoin(n):
    count = 0
    while n > count:
        flip = random.randint(0, 1)
        if flip == 0:
            print "Tails"
        elif flip == 1:
            print "Heads"
        count += 1


flipcoin(n)
