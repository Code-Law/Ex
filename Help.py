c=0
L=[]
Num = int(input("Input number:"))
for i in range (2*Num):
    if i%3 != 0 and i%5 !=0:
        c=c+1
        L.append(i)
    while c==Num:
        break
print(L)