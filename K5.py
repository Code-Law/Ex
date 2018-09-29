c = 0
s = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 9 != 0:
        c = c + 1
        s = s + i
print(c)
print(s)
print(s / c)
