import random
R = random.randint(0, 20)
i = 0
while i < 5:
    a = int(input("Please input an integer:"))
    if a > R:
        print("Bigger")
    elif a < R:
        print("Smaller")
    else:
        print("You Win!")
    i = i + 1
    if i == 5:
        print("Game Over!")
