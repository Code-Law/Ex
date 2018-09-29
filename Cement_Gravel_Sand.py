Type_of_sack = []

CementWeight = []
GravelWeight = []
SandWeight = []

RejectCementWeight = []
RejectGravelWeight = []
RejectSandWeight = []

Reject_Count_of_Cement = 0
Reject_Count_of_Gravel = 0
Reject_Count_of_Sand = 0

Count_of_Cement = 0
Count_of_Gravel = 0
Count_of_Sand = 0

while True:
    s = int(input('input the type your sack (1=Cement; 2=Gravel;3 =Sand):'))

    if s == 1:
        C_Weight = float(input('Weight:'))
        if C_Weight > 24.9 and C_Weight < 25.1:
            Count_of_Cement = Count_of_Cement + 1
            CementWeight.append(s)
        else:
            print('Weight out of range')
            Reject_Count_of_Cement = Reject_Count_of_Cement + 1
            RejectCementWeight.append(s)

    elif s == 2:
        C_Weight = float(input('Weight:'))
        if C_Weight > 24.9 and C_Weight < 25.1:
            Count_of_Cement = Count_of_Cement + 1
            CementWeight.append(s)
        else:
            print('Weight out of range')
            Reject_Count_of_Cement = Reject_Count_of_Cement + 1
            RejectCementWeight.append(s)

    elif s == 3:
        C_Weight = float(input('Weight:'))
        if C_Weight > 24.9 and C_Weight < 25.1:
            Count_of_Cement = Count_of_Cement + 1
            CementWeight.append(s)
        else:
            print('Weight out of range')
            Reject_Count_of_Cement = Reject_Count_of_Cement + 1
            RejectCementWeight.append(s)

    else:
        exit()

print("CementWeight:", CementWeight)
print("Count_of_Cement", Count_of_Cement)
print("Reject_Count_of_Cement", Reject_Count_of_Cement)
