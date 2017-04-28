# 2017-04-04
# Ex Description:
# Find the Sum of S. S=a+aa+aaa+aaaa+aa…a. a∈N. a=[1,9].There are n addend.
# Input a and n. (eg: if a=3,n=5: thus: S=3+33+333+3333+33333),Output S.

def fib2(a, n):
    if n == 1:
        return a
    else:
        return (fib2(a, n - 1) + (a * 10**(n - 1)))

q=[]
a=int(input("Please input a:"))
n=int(input("Please input n:"))
for i in range(1,n+1):
    print("Number",i,":",fib2(a,i))
    q.append(fib2(a,i))
print("Sum=",sum(q))
