import math

iData = []
f = []
c = 10
while c < 90001:
    iData.append(c)
    c = c + 1
for i in range(len(iData)):
    a = iData[i]
    m = list(str(iData[i]))
    for index, item in enumerate(m):
        m[index] = int(item)
    l = len(m)
    s = 0
    for i in range(0, l):

        s = s + math.factorial(m[i])
    if a == s:
        f.append(a)
print("Final list:", f)
