import matplotlib.pyplot as plt
import numpy as np

# Generate data points
x = np.linspace(0.1, 10, 400)  # 400 points between 0.1 and 10 (0.1 to avoid log(0) issue)

# Define different mathematical functions
y_sin = np.sin(x)                 # Sine curve
y_cos = np.cos(x)                 # Cosine curve
y_exp = np.exp(x / 3)             # Exponential curve
y_log = np.log(x)                 # Logarithmic curve
y_quad = x**2                     # Quadratic curve

# Plot each curve with different styles
plt.figure(figsize=(10, 6))

# Sine Curve
plt.plot(x, y_sin, label='Sine', color='blue', linestyle='-', linewidth=2)

# Cosine Curve
plt.plot(x, y_cos, label='Cosine', color='red', linestyle='--', linewidth=2)

# Exponential Curve
plt.plot(x, y_exp, label='Exponential', color='green', linestyle='-.', linewidth=2)

# Logarithmic Curve
plt.plot(x, y_log, label='Logarithmic', color='purple', linestyle=':', linewidth=2)

# Quadratic Curve
plt.plot(x, y_quad, label='Quadratic', color='orange', linestyle='-', linewidth=2)

plt.title('Different Mathematical Curves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

