import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-1, 1])
ax.axis('off')

plt.savefig('../outputs/visual4.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()
