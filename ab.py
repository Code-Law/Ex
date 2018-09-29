n = 0
a = 0


def f(n):
    if n == 1:
        return a
    else:
        return f(n - 1) * 10 + n * a


n = int(input("input n:"))
a = int(input("input a:"))
print(f(n))
