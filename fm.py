def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

i = 146
k = []
s = 0
while i > 145:
    j = list(str(i))
    for a in range(len(j)):
        k.append(int(j[a]))
        for b in range(len(k)):
            p = k[b]
            s = s + f(p)
        if s == i:
            print(s)
            break
    i = i + 1
