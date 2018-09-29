import random


def guess():
    num = random.randint(0, 10)
    guess = False

    while guess == False:
        guess_num = int(input("Enter the guessed number :"))
        if guess_num > num:
            print("Bigger,Retry\n")
        elif guess_num < num:
            print("Smaller,Retry\n")
        else:
            guess = True
            print("Congratulations!")


guess()
