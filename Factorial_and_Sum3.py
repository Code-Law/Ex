def f(n=1):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)


for p in range(100, 100000):
    s = 0
    newlist = []
    numbers = []
    l = sorted(str(p))
    for e in l:
        newlist.append(int(e))
        # print(newlist)
        s = s + f(e)
        # print(s)
        if p == s:
            print(p)
            break
# print(f(8))