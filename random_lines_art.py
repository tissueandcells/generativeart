import matplotlib.pyplot as plt
import numpy as np

def generate_art(num_lines, max_line_length, randomness, dense_area, sparse_area, dense_area_multiplier):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    for _ in range(num_lines):
        x = np.random.uniform(0, 100)
        y = np.random.uniform(0, 100)
        angle = np.random.uniform(0, 2 * np.pi)
        line_length = np.random.uniform(max_line_length / 2, max_line_length)
        x_end = x + line_length * np.cos(angle) + np.random.uniform(-randomness, randomness)
        y_end = y + line_length * np.sin(angle) + np.random.uniform(-randomness, randomness)

        if dense_area['x_min'] <= x <= dense_area['x_max'] and dense_area['y_min'] <= y <= dense_area['y_max']:
            for _ in range(dense_area_multiplier):
                ax.plot([x, x_end], [y, y_end], color='black', linewidth=1)
        else:
            ax.plot([x, x_end], [y, y_end], color='black', linewidth=1)

    plt.savefig('../outputs/random_lines_300dpi.png', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.show()

generate_art(
    num_lines=1000,
    max_line_length=30,
    randomness=5,
    dense_area={'x_min': 30, 'x_max': 50, 'y_min': 50, 'y_max': 70},
    sparse_area={'x_min': 70, 'x_max': 90, 'y_min': 70, 'y_max': 90},
    dense_area_multiplier=15
)
