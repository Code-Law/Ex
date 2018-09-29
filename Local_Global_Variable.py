x=3
def f(x):
    print('x is equal to',x)
    x=2
    print('Local variable x now is changed to',x)
f(x)
print('x is always equal to',x)
