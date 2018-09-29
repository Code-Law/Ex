while True:
    n = input("Please input an binary number:")
    a = list(n)
    print(a)
    for index, item in enumerate(a):
        a[index] = int(item)
    print(a)
    s = 0
    length = len(a)
    print("length=", length)
    for i in range(0, length):
        s = s + (a[i] * (2 ** (length - 1)))
        length = length - 1
        # print(s)
    print(s)
