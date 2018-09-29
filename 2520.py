for n in range(1000, 3000):
    i = 2
    while n % i == 0:
        i = i + 1
        if i == 11:
            print(n)
            break
