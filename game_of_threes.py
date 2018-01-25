num = int(raw_input(">Enter the number:\n"))
while True:
    if num == 3:
        break
    elif num % 3 == 0:
        num = num / 3
    else:
        num += 1
    print num
