i = 0
d = 0
l = ["A", "b", "C", "D", "e"]
dsp = ["Are", "Bright", "Cool", "DoING", "Error"]
la = []
ind = 0
for i in range(5):
    la.append(l[i].lower())


def dc(d):
    d = input("Device name:")
    if d.lower() in la:
        print("Y")
        ind = la.index(d.lower())
        print(ind)
        print(dsp[ind])
    else:
        print("N")


dc(d)
