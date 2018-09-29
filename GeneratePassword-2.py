# generate a password with length "passlen" with no duplicate characters in the password
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
t = list(s)
p = []
for i in range(16):
    n = random.randint(0, 73)
    p.append(t[n])
print(p)
print("".join(p))
