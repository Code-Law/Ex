import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import csv
#____________________________________

# plt.plot([1,2,3],[4,6,3])
# plt.show()
#____________________________________
#
# x=[1,2,3]
# y=[4,6,3]
#
# a=[1,2,3]
# b=[3,2,1]
#
# plt.plot(x,y,label='First Line')
# plt.plot(a,b,label='Second Line')
# plt.xlabel('Plot Number')
# plt.ylabel('Important var')
# plt.title('Graph \n Nice')
# plt.legend()
# plt.show()
#____________________________________

#x=[2,4,6,8,10]
#y=[4,6,3,7,8]
#
#a=[1,3,5,9,11]
#b=[7,8,2,4,2]
#
#
#plt.bar(x,y,label='XY',color='c')
#plt.bar(a,b,label='AB',color='g')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Graph \n Nice')
#plt.legend()
#plt.show()
#____________________________________

age=[45,78,56,90,46,83,35,78,90,72,69,99,67,69,72,71,89,84,55,42,60,58]
ids=[x for x in range(len(age))]
plt.bar(ids,age)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph \n 2017')
plt.show()
#____________________________________

# age=[45,78,56,90,6,83,35,78,90,12,69,99,67,29,72,71,89,84,55,42,60,58]
# bins=[0,10,20,30,40,50,60,70,80,90,100]
#
# fig = plt.figure(figsize=(12,6), dpi=60, facecolor="white")
# plt.hist(age,bins,histtype='bar',rwidth=0.8)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Graph \n 2017')
# plt.show()
#____________________________________

#x=[2,4,6,8,10]
#y=[4,6,3,7,8]
#
#fig = plt.figure(figsize=(12,8), dpi=60, facecolor="white")
#
#plt.scatter(x,y,label='skitscat',color='g',s=100,marker='o')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Graph \n 2017')
#plt.show()

#____________________________________



#____________________________________




