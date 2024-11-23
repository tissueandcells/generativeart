import matplotlib.pyplot as plt
import numpy as np

def draw_spiral(ax, center, radius, num_turns, color):
    theta = np.linspace(0, 2 * np.pi * num_turns, 1000)
    r = np.linspace(0, radius, 1000)
    x = center[0] + r * np.cos(theta)
    y = center[1] + r * np.sin(theta)
    ax.plot(x, y, color=color, lw=2)

def draw_fractal(ax, center, radius, depth, max_depth, color):
    if depth > max_depth:
        return
    draw_spiral(ax, center, radius, depth, color)
    new_radius = radius / 2
    for angle in np.linspace(0, 2 * np.pi, 6, endpoint=False):
        new_center = (center[0] + new_radius * np.cos(angle), center[1] + new_radius * np.sin(angle))
        draw_fractal(ax, new_center, new_radius, depth + 1, max_depth, color)

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_aspect('equal')
ax.axis('off')

colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']

np.random.seed(42)
for _ in range(15):
    center = (np.random.uniform(-1, 1), np.random.uniform(-1, 1))
    radius = np.random.uniform(0.1, 0.5)
    color = np.random.choice(colors)
    draw_fractal(ax, center, radius, 1, 4, color)

plt.savefig('../outputs/fractal_design_300dpi.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()

