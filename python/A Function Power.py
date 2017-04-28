def s(n):
    return n*n

q=[]
x=int(input("Please input x:"))
for i in range(1,x+1):
    print("Number:",s(i))
    q.append(s(i))
print("Sum=",sum(q))
