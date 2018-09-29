while True:
    l = []
    n = int(input("Please input a number:"))
    while n >= 1:
        r = n % 2
        n = n // 2
        l.append(r)
        k = l[::-1]
        for i in range(len(k)):
            k[i] = str(k[i])
        k = "".join(k)
    print(k)
