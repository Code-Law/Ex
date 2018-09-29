from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

y=2*x+3
z=3
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap='rainbow')
plt.show()