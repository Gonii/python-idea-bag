doors = []


def toggle(n):
    if doors[n] == "closed":
        doors[n] = "open"
    elif doors[n] == "open":
        doors[n] = "closed"


for i in range(100):
    doors.append("closed")


def first_pass():
    for i in range(100):
        toggle(i)


def second_pass():
    for i in range(0, 100, 2):
        toggle(i)


def third_pass():
    for i in range(0, 100, 3):
        toggle(i)


def main():
    first_pass()
    second_pass()
    third_pass()


main()
count = 0
for word in doors:
    print ("Door" + str(count) + "-" + word)
    count += 1
