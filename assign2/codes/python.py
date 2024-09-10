import numpy as np
import matplotlib.pyplot as plt

def read_vertices(filename):
    data = np.loadtxt(filename)
    if data.shape[1] != 2:
        raise ValueError("File should contain pairs of (x, y) coordinates.")
    return data

def plot_parallelogram(vertices):
    if vertices.shape[0] != 4:
        raise ValueError("The file should contain exactly 4 pairs of (x, y) coordinates.")
    x = vertices[:, 0]
    y = vertices[:, 1]
    x = np.append(x, x[0])  # Append the first x-coordinate to the end to close the loop
    y = np.append(y, y[0])  # Append the first y-coordinate to the end to close the loop
    
    labels = ['A', 'B', 'C', 'D']
    
    plt.figure()
    plt.plot(x, y, 'bo-')  # Plot vertices and connect them with lines
    plt.fill(x, y, 'cyan', alpha=0.3)  # Fill the parallelogram with color
    
    # Label each vertex with its name and coordinates
    for i in range(4):
        plt.text(x[i], y[i], f'{labels[i]} ({x[i]:.1f}, {y[i]:.1f})', fontsize=12, ha='right', color='black')

   
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.axis([-5, 9, -2, 8])
    plt.show()

if __name__ == "__main__":
    vertices_file = 'parallelogram_coordinates.txt'
    vertices = read_vertices(vertices_file)
    plot_parallelogram(vertices)

