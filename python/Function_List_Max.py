b=0
n=[]
def a(n=[]):
    b=0
    for i in range(3):
        n.append(int(input("input:")))
        while n[i]>b:
            b=n[i]
        i=i+1
    print(b)
while True:
    a(n=[])
