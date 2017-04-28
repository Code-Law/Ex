def ca():
    tn=0
    an=0
    for i in range(3):
        n=int(input("Please input a number:"))
        tn=tn+n
        i=i+1
    an=float(tn/i)
    print(an)

while True:
    ca()
