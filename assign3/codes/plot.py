import matplotlib.pyplot as plt

# Function to read points from a file
def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers (x and y coordinates)
            x, y = map(float, line.split())
            points.append((x, y))
    return points

# Read points from 'data.txt'
points = read_points_from_file('data.txt')

# Separate the points into x and y coordinates
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Plotting the line
plt.plot(x_coords, y_coords, marker='o', label='Line through points')

# Label each point
for i, (x, y) in enumerate(points):
    plt.text(x, y, f'({x}, {y})', fontsize=12, ha='right')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line with equal intercepts')

# Add some padding to the axes to avoid coincidence of points with axes
x_padding = (max(x_coords) - min(x_coords)) * 0.1
y_padding = (max(y_coords) - min(y_coords)) * 0.1

plt.xlim(min(x_coords) - x_padding, max(x_coords) + x_padding)
plt.ylim(min(y_coords) - y_padding, max(y_coords) + y_padding)

# Show legend and grid
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

