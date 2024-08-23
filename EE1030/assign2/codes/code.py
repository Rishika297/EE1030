import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load coordinates from the file using np.loadtxt
data = np.loadtxt('parallelogram_coordinates.txt', delimiter=',', dtype=int)

# Extract x and y coordinates
x = data[:, 0]
y = data[:, 1]

# Create a new figure and axis
fig, ax = plt.subplots()

# Create a polygon using the vertices
parallelogram = patches.Polygon(list(zip(x, y)), closed=True, fill=None, edgecolor='r')

# Add the polygon to the plot
ax.add_patch(parallelogram)

# Set the limits of the plot
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 10)

# Set equal scaling
ax.set_aspect('equal')

# Label the axes
plt.xlabel('X')
plt.ylabel('Y')

# Add grid
plt.grid(True)

# Add a title
plt.title('Parallelogram Plot')

# Annotate each vertex with its coordinate
for (xi, yi) in zip(x, y):
    ax.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(5,5), ha='center')

# Show the plot
plt.show()

