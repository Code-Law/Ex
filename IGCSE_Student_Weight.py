Student_Weight = []
Student_Name = []
for i in range(3):
    Check_Weight = int(input("Student_Weight:"))
    while Check_Weight > 100 or Check_Weight < 15:
        print("Are you kidding me? Please input again!")
        Check_Weight = int(input("Student_Weight:"))
    else:
        Student_Weight.append(Check_Weight)
    Student_Name.append(str(input("Student_Name:")))
for i in range(3):
    print(Student_Name[i], Student_Weight[i])