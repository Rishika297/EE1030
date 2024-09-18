import matplotlib.pyplot as plt

# Function to read vertices from the file
def read_vertices_from_file(filename):
    vertices = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            vertices.append((x, y))
    return vertices

# Function to plot a parallelogram
def plot_parallelogram(vertices, x_limits=None, y_limits=None):
    vertices.append(vertices[0])  # Close the loop by appending the first vertex at the end
    x, y = zip(*vertices)
    
    plt.figure()
    plt.plot(x, y, 'b-')  # Blue line for the parallelogram
    plt.fill(x, y, 'skyblue', alpha=0.3)  # Light blue fill
    plt.scatter(x, y, color='red')  # Red dots for vertices

    # Labeling vertices
    for i, (xi, yi) in enumerate(vertices[:-1]):
        plt.text(xi, yi, f'({xi}, {yi})', fontsize=12, ha='right')
    
    # Set axis limits if provided
    if x_limits:
        plt.xlim(x_limits)
    if y_limits:
        plt.ylim(y_limits)

    # Setting the aspect ratio to equal
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Parallelogram')
    plt.grid(True)
    plt.show()

# Main code
vertices = read_vertices_from_file('pc.txt')

# Example: setting x-axis limit from -1 to 5, and y-axis limit from -1 to 5
plot_parallelogram(vertices, x_limits=(-5, 9), y_limits=(-2, 9))

