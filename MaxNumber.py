#Input 6 integer.Output the biggest one.
m=0
number=[]
for i in range(6):
    num=int(input("number:"))
    number.append(num)
    if number[i]>m:
        m=number[i]
print(m)
