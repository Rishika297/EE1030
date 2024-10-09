import numpy as np
import matplotlib.pyplot as plt

# Function to read data from the file
def read_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Parse the center
    center = tuple(map(float, lines[0].strip().split(':')[1].strip().split(',')))
    
    # Parse the radius
    radius = float(lines[1].strip().split(':')[1].strip())

    # Parse the points
    points_line = lines[2].strip().split(':')[1].strip()
    points = [tuple(map(float, p.strip().strip('()').split(','))) for p in points_line.split('), (')]
    
    return center, radius, points

# Read the circle parameters from data.txt
center, radius, points = read_data('data.txt')

# Create a range of angles for the circle
theta = np.linspace(0, 2 * np.pi, 100)

# Parametric equations for the circle
x_circle = radius * np.cos(theta) + center[0]
y_circle = radius * np.sin(theta) + center[1]

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, label='Circle', color='blue')
plt.scatter(center[0], center[1], color='purple', label=f'Center {center}')
for point in points:
    plt.scatter(*point, label=f'Point {point}')

# Draw radius lines to each point and label it
for point in points:
    plt.plot([center[0], point[0]], [center[1], point[1]], color='orange', linestyle='--')
    # Label the radius
    mid_x = (center[0] + point[0]) / 2
    mid_y = (center[1] + point[1]) / 2
    plt.text(mid_x, mid_y, f' Radius = {radius:.2f}', fontsize=10, color='orange', verticalalignment='bottom')

# Label points
for point in points:
    plt.text(point[0], point[1], f'  {point}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

# Set equal aspect ratio
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

