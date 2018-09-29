import random
import os
os.system(start "Users/bone/Desktop/StratovariusForever.mp3")

j = 0
m = 0
bottom = int(input("Bottom Number:"))
top = int(input("Top Number:"))

for j in range(0, 3):
    i = 0
    R = random.randint(bottom, top)
    print("round", j + 1)
    print("—————— see the cute cut-off line ——————")

    while i < 4:
        a = int(input("Guess:"))
        if a > R:
            print("Bigger")
        elif a < R:
            print("Smaller")
        else:
            print("You Win!")
            m = m + 1
            break

        i = i + 1
        if i == 4:
            # print("game over")
            print("The number is", R)
            print("——————————————————————")
    # print("your point is", m)
    if j == 3:
        print("Game Over")