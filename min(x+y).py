a = 10
b = 1
while a ** 2 < 200:
    if (a ** 2 - b ** 2) % 2 != 0:
        pass
    else:
        print(a, b, a * a)
    a = a + 1
