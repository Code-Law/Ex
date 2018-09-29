def top_left(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) ** 2 - 2*(n - 1)

p = 0
p = int(input("Please input p:"))
print(top_left(p))
