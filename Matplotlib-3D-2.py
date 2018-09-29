from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

z=
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()