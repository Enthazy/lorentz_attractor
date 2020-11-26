import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


step = 0.01
epoch = 10000

# Need one more for the initial values
x_hist = []
y_hist = []
z_hist = []

x_cur, y_cur, z_cur = (0., 1., 1.05)

for i in range(epoch):
    x_dot, y_dot, z_dot = lorenz(x_cur, y_cur, z_cur)
    x_hist.append(x_cur)
    y_hist.append(y_cur)
    z_hist.append(z_cur)

    x_cur += x_dot * step
    y_cur += y_dot * step
    z_cur += z_dot * step

# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x_hist, y_hist, z_hist, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")


plt.show()