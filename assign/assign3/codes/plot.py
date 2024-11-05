import numpy as np
import matplotlib.pyplot as plt
def read_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    center = tuple(map(float, lines[0].strip().split(':')[1].strip().split(',')))
    radius = float(lines[1].strip().split(':')[1].strip())
    points_line = lines[2].strip().split(':')[1].strip()
    points = [tuple(map(float, p.strip().strip('()').split(','))) for p in points_line.split('), (')]
    return center, radius, points
center, radius, points = read_data('data.txt')
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = radius * np.cos(theta) + center[0]
y_circle = radius * np.sin(theta) + center[1]
plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, label='Circle', color='blue')
plt.scatter(center[0], center[1], color='purple', label=f'Center {center}')
for point in points:
    plt.scatter(*point, label=f'Point {point}')
for point in points:
    plt.plot([center[0], point[0]], [center[1], point[1]], color='orange', linestyle='--')
    mid_x = (center[0] + point[0]) / 2
    mid_y = (center[1] + point[1]) / 2
    plt.text(mid_x, mid_y, f' Radius = {radius:.2f}', fontsize=10, color='orange', verticalalignment='bottom')
for point in points:
    plt.text(point[0], point[1], f'  {point}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
plt.axis('equal')
plt.xlim(center[0] - radius - 1, center[0] + radius + 1)
plt.ylim(center[1] - radius - 1, center[1] + radius + 1)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()

