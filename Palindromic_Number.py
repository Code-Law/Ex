# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers

a, b, f = 0, 0, []
for a in range(100, 1000):
    for b in range(100, 1000):
        l = list(str(a * b))
        i = l[::-1]
        if (a * b) > 100000:
            if l == i:
                f.append(a * b)
print(max(f), a, b)
# print(a * b, a, b)
