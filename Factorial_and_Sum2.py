def f(n):
    z = 1
    for i in range(int(n)):
        z = z * (i + 1)
    return z


for p in range(100, 100000):
    s = 0
    newlist = []
    numbers = []
    l = sorted(str(p))
    for e in l:
        newlist.append(int(e))
        #print(newlist)
        s = s + f(e)
        #print(s)
        if p == s:
            print(p)
            break
# print(f(8))
