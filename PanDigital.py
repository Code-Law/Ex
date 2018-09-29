def IsPandigital(n):
    n = int(input("Input n:"))
    print("n is:", n)
    a = sorted(str(n))
    print("a is:", a)
    print("a[0] is:", a[0])
    print("a[1] is:", a[1])
    for i in range(10):
        if a[i] == a[i + 1]:
            print("NO.")
    else:
        print("Yes.")


n = 0
while True:
    IsPandigital(n)
