import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')

rect = patches.Rectangle((0, 0), 1, 1, edgecolor='black', facecolor='none', lw=2)
ax.add_patch(rect)

lines = [
    [(0, 0), (1, 1)], [(0, 1), (1, 0)],
    [(0.5, 0), (0.5, 1)], [(0, 0.5), (1, 0.5)],
    [(0, 0), (0.75, 1)], [(0.25, 0), (1, 1)],
    [(0, 1), (0.25, 0)], [(0.75, 0), (1, 1)]
]

for line in lines:
    ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], color='black')

plt.savefig('../outputs/visual3.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()
