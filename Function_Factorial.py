def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


x = int(input("Please input a positive integer:"))
while x < 0:
    x = int(input("Please input a positive integer:"))
print(factorial(x))
