days = 7
Yield1 = []
Yield2 = []
maxyield = 0
totalyield = 0
for ID in range(1):
    Id = input("please input the id of the cow：")
    while (len(Id)) != 3 or ((Id[0:3]).isdigit() == 0) or ((int(Id)) > 6):
        Id = input("please input the id of the cow again：")
    for day in range(1, 8):
        yield1 = float(input("please input the first yield of day %d:" % (day)))
        Yield1.append(yield1)
        yield2 = float(input("please input the second yield of day %d:" % (day)))
        Yield2.append(yield2)
        totalyield = int(totalyield + yield1 + yield2)
    print(Yield1, Yield2)
    a = [0] * 14
    for i in range(days):
        a[2 * i] = Yield1[i + 7 * ID]
        a[2 * i + 1] = Yield2[i + 7 * ID]

    if maxyield < totalyield:
        maxyield = totalyield
    averageyield = int(totalyield / 7)
    print(a)
    print("the total weekly volume of cow", Id, "is", totalyield)
    print("the average yield in a week for cow", Id, "is", averageyield)
