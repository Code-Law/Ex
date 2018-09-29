S=0
# Define a function to calculate factorial
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
#Convert an integer to list with each item integer
L=list(str(328))
print(L)
for index, item in enumerate(L):
    L[index] = int(item)
print(L)
#Calculate the sum of factorials of each bit
Length_Count=len(L)
for i in range(Length_Count):
    S=S+f(L[i])
print("S is:",S)
if S==328:
    print("Yes")
else:
    print("No")
