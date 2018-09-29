n = 100
i = 2
f = []
while i * i < 100:
    while (n % i) == 0:
        n = n / i
        if i not in f:
            f.append(i)
    i = i + 1
print(f)