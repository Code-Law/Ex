def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


i = 1
while i > 0:
    fi = f(i)
    digits = list(str(fi))
    if len(digits) == 8:
        print(i)
        print(f(i))
        break
    else:
        i = i + 1
