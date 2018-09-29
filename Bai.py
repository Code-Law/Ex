Yield1 = [0] * 7
Yield2 = [0] * 7
totalyield = 0
MaxYield = 0
for ID in range(1):
    Id = input("please input the id of the cow：")
    while (len(Id)) != 3 or ((Id[0:3]).isdigit() == 0):
        Id = input("please input the id of the cow again：")
    for day in range(1, 3):
        yield1 = float(input("please input the first yield of the day %d:" % (day)))
        Yield1[day] = yield1
        yield2 = float(input("please input the second yield of the day %d:" % (day)))
        Yield2[day] = yield2

        totalyield = totalyield + yield1 + yield2
        averageyield = float(totalyield / 2)

        # if totalyield > MaxYield:
        #     MaxYield = totalyield

    print("the total weekly volume of cow", Id, "is", totalyield)
    print("the average yield in a week for cow", Id, "is", averageyield)
