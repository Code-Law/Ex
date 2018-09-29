import matplotlib.pyplot as plt #绘图用的模块  
from mpl_toolkits.mplot3d import Axes3D #绘制3D坐标的函数  
import numpy as np  
  
def f1(x,y):  
    return -3*x-4*y+10

def f2(x,y):  
    return (-2*x-5*y+15)/3
  
def f3(x,y):  
    return (-2*x-3*y)/4

fig1=plt.figure()#创建一个绘图对象  
ax=Axes3D(fig1)#用这个绘图对象创建一个Axes对象(有3D坐标)  
X,Y=np.mgrid[0:4:40j,0:4:40j]#从-2到2分别生成40个取样坐标，并作满射联合  
Z1=f1(X,Y)#用取样点横纵坐标去求取样点Z坐标
Z2=f2(X,Y)#用取样点横纵坐标去求取样点Z坐标   
Z3=f3(X,Y)#用取样点横纵坐标去求取样点Z坐标 
plt.title("This is main title")#总标题  
ax.plot_surface(X, Y, Z1, rstride=1, cstride=1,alpha=0.5)#用取样点(x,y,z)去构建曲面
ax.plot_surface(X, Y, Z2, rstride=1, cstride=1,alpha=0.5)#用取样点(x,y,z)去构建曲面
ax.plot_surface(X, Y, Z3, rstride=1, cstride=1,alpha=0.5)#用取样点(x,y,z)去构建曲面

plt.plot(x,y,f1(x,y),'go',markersize=10,)
plt.plot(x2,f1(x2),'go',markersize=10)
plt.plot(x3,f2(x3),'go',markersize=10)

plt.fill([x1,x2,x3,x1],[y1,y2,y3,y1],'red',alpha=0.5)

ax.set_xlabel('x label', color='r')  
ax.set_ylabel('y label', color='g')  
ax.set_zlabel('z label', color='b')#给三个坐标轴注明  
plt.show()#显示模块中的所有绘图对象  