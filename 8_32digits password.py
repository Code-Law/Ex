import random

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"
a = list(s)
b = []
digits = int(input("Input Password length(8-32):"))
while digits < 8 or digits > 32:
    digits = int(input("Out of range, please input again:"))
contain = int(input("What kind of Characters does the password contains?(letters:1; numbers:2; Symbol:3; all: 4)"))
time = 0
if contain != 4:
    contain2 = int(input("What kind of Characters does the password contains?(letters:1; numbers:2; Symbol:3; all: 4)"))
    while contain == contain2:
        contain2 = input("this is the same as the last one you contain.")
if contain == 1:
    if contain2 == 2:
        for i in range(0, digits):
            n = random.randint(0, 62)
            b.append(a[n])
        print("".join(b))
        time = (63 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
    elif contain2 == 3:
        for i in range(0, digits):
            n = random.randint((0, 52), (63, 73))
            b.append(a[n])
        print("".join(b))
        time = (62 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
    elif contain2 == 4:
        for i in range(0, digits):
            n = random.randint(0, 52)
            b.append(a[n])
        print("".join(b))
        time = (52 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
elif contain == 2:
    if contain2 == 1:
        for i in range(0, digits):
            n = random.randint(0, 62)
            b.append(a[n])
        print("".join(b))
        time = (63 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
    elif contain2 == 3:
        for i in range(0, digits):
            n = random.randint(52, 73)
            b.append(a[n])
        print("".join(b))
        time = (21 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
    elif contain2 == 4:
        for i in range(0, digits):
            n = random.randint(53, 62)
            b.append(a[n])
        print("".join(b))
        time = (11 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
elif contain == 3:
    if contain2 == 1:
        for i in range(0, digits):
            n = random.randint((0, 52), (63, 73))
            b.append(a[n])
        print("".join(b))
        time = (62 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
    elif contain2 == 2:
        for i in range(0, digits):
            n = random.randint(53, 73)
            b.append(a[n])
        print("".join(b))
        time = (21 ** digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
    elif contain2 == 4:
        for i in range(0, digits):
            n = random.randint(64, 73)
            b.append(a[n])
        print("".join(b))
        time = (10 * digits) - 1
        print("there are", time, "times that the computer can guess wrong at most.")
elif contain == 4:
    for i in range(0, digits):
        n = random.randint(0, 73)
        b.append(a[n])
    print("".join(b))
    time = (73 ** digits) - 1
    print("there are", time, "times that the computer can guess wrong at most.")
if time < (10 ** 10):
    print("the safety level of this password is 1")
elif time > (10 ** 15) and time < (10 ** 20):
    print("the safety level of this password is 2")
elif time > (10 ** 20) and time < (10 ** 30):
    print("the safety level of this password is 3")
elif time > (10 ** 30) and time < (10 ** 40):
    print("the safety level of this password is 4")
elif time > (10 ** 40) and time < (10 ** 50):
    print("the safety level of this password is 5")
else:
    print("the safety level of this password is 6")
