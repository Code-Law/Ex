# final list
def lis():
    print(a, len(b), b)


# Menu
def smenu():
    x = input("1=choose lesson,2=final list,Please input your choice:")
    if x == 1:
        sbj()
    else:
        lis()


# choose your lesson
b = []


def sbj():
    s = ["Math", "English", "Geography", "Physics", "Chemistry", "History", "Economics"]
    print("At least three subjects please!")
    while len(b) < 7:
        # print(b)
        p = input(
            "Choose your subjects,(Math,English,Geography,Physics,Chemistry,History,Economics),Everyone should choose at least three subjects:")

        # Subject not found
        while p not in s:
            p = input("Subject not found,please input:")

        # Add subjects
        if p not in b:
            b.append(p)
        elif
        else:
            print("You have already chosen it")


# check student_ID
while True:
    a = int(input("please input your student_ID:"))
    if a >= 20180001 and a <= 20189999:
        sbj()
    else:
        print("Retry!")