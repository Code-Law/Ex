n = 60
i = 1
factors = []
while i < n:
    while (n % i) == 0:
        n = n / i
        print(n)
        factors.append(i)
    i = i + 1
print(factors)
