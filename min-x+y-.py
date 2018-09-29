##Find the smallest x + y with integers x > y > 0 such that x + y, x − y are all perfect squares.
##x+y=a^2; x-y=b^2.
a=10
b=1
while(a>9 and a<20):
    if ((a**2-b**2)%2!=0):
        pass
    else:
        print(a,b)
    a=a+1
    
