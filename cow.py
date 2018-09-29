identity = []
yeild = []
ErrCheck = 0
weeklyyeild = 0
for i in range(2):

    y = input("identity:")  # it's the input of identity code
    while len(y) != 3:  # error checking
        y = input("error!Please reinput:")
    identity.append(y)

    I = input("yeild:")
    while I.isdigit == False:
        I = input(" Input yeild again(only numbers):")
    weeklyyeild = weeklyyeild + int(I)
    averageyeild = weeklyyeild // 2  # making output a whole number
    yeild.append(float(I))  # making output to one decimal
i = i + 1
print("identity:", identity, "yeild:", yeild, "weeklyyeild:", weeklyyeild, "averageyeild:", averageyeild)
