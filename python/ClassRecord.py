Student_Name=[]
Student_State=[]
GreenCount=0
RedCount=0
#
for i in range(3):
    Name=input("Please input your name:")
    Student_Name.append(Name)
    while Name.isalpha() == False:
        Name=input("Error Type! Please input Name:")

    State=input("Please input your state:Red,Green:")
    while State.lower()!='red' and State.lower()!='green':
        State=input("Please input a valid choice:")
    Student_State.append(State)

    if State.lower() == 'green':
        GreenCount=GreenCount+1
        print("Green:",GreenCount)
        print("Red:",RedCount)
    elif State.lower() == 'red':
        RedCount=RedCount+1
        print("Green:",GreenCount)
        print("Red:",RedCount)
#
print("=======================")
print("Here is the list:")
for i in range(3):
    print("Name:",Student_Name[i],";","State:",Student_State[i])
    print("=======================")
#
print("=======================")
print("Here is the Result:")
print("Green:",GreenCount)
print("Red:",RedCount)