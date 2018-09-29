def Student():
    Student_num = int(input("please input your student number:"))
    while Student_num < 4990 or Student_num > 5200:
        Student_num = int(input("your student number is out of range, please input again!"))
    while Student_num in Student_Numbers:
        Student_num = int(input("this student number has already been inputted, please input again!"))
    Student_Numbers.append(Student_num)
    Subject_Choice()


def Subject_Choice():
    global Fundamentals
    Fundamentals = 3
    Subject_choices = []
    subject_1 = input("what's your first subject choice?")
    while subject_1 not in Subjects:
        subject_1 = input("this is not a choice, please input again:")
    Subject_choices.append(subject_1)
    subject_2 = input("what's your second subject choice?")
    while subject_2 not in Subjects:
        subject_2 = input("this is not a choice, please input again:")
    while subject_2 == subject_1:
        subject_2 = input("this subject has already been inputted, please input again:")
    Subject_choices.append(subject_2)
    subject_3 = input("what's your third subject choice?")
    while subject_3 not in Subjects:
        subject_3 = input("this is not a choice, please input again:")
    while subject_3 == subject_1 or subject_3 == subject_2:
        subject_3 = input("this subject has already been inputted, please input again:")
    Subject_choices.append(subject_3)
    if "Geography" in Subject_choices:
        Fundamentals = Fundamentals - 1
    if "History" in Subject_choices:
        Fundamentals = Fundamentals - 1
    if "Economics" in Subject_choices:
        Fundamentals = Fundamentals - 1
    Foundamental_num = Fundamentals
    Subject_choice = Subject_choices
    print(Foundamental_num + 1)
    print("you have chosen %0d fundamental subjects" % (Foundamental_num+1))
    print(Subject_choice)


Student_Numbers = []
Subject_choice = []
Subjects = ["Math", "English", "Geography", "Physics", "Chemistry", "History", "Economics"]
for i in range(210):
    Student()
    # print("your subject choices are:")
    # print(Subject_choices)
