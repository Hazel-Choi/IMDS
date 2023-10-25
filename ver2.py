import numpy as np
import matplotlib.pyplot as plt

##visualize the graph
# Define the function
def f(x, y):
    return np.exp(-((x**2 + y**2) / 30)) * np.sin((x**2 + y**2) / 5)

# Generate values for x and y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create a 2D contour plot
plt.contourf(X, Y, Z, cmap='viridis', levels=50)  # You can adjust the number of contour levels as needed
plt.colorbar(label='f(x, y)')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Contour Plot of f(x, y)")

# Show the plot
plt.show()


#calculate the gradient at the point(5,-6)
def gradient(x, y):
    df_dx = ((-2 * x) / 30) * np.exp(-((x**2 + y**2) / 30)) * np.sin((x**2 + y**2) / 5) + np.exp(-((x**2 + y**2) / 30)) * (2 * x / 5) * np.cos((x**2 + y**2) / 5)
    df_dy = ((-2 * y) / 30) * np.exp(-((x**2 + y**2) / 30)) * np.sin((x**2 + y**2) / 5) + np.exp(-((x**2 + y**2) / 30)) * (2 * y / 5) * np.cos((x**2 + y**2) / 5)
    return df_dx, df_dy

x_start, y_start = 5, -6

# Compute the gradient at the starting point
grad_x, grad_y = gradient(x_start, y_start)

# Calculate the Euclidean norm of the gradient vector
gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

# Check the direction
if grad_x > 0 and grad_y > 0:
    print("The gradient points away from the origin, moving further.")
elif grad_x < 0 and grad_y < 0:
    print("The gradient points toward the origin, moving closer.")
else:
    print("The gradient has components in different directions, the movement depends on their relative magnitudes.")


# Determine the relative magnitude
if gradient_magnitude > 0:
    relative_magnitude_x = grad_x / gradient_magnitude
    relative_magnitude_y = grad_y / gradient_magnitude
else:
    relative_magnitude_x = 0
    relative_magnitude_y = 0

print("Gradient Magnitude:", gradient_magnitude)
print("Relative Magnitude in X-direction:", relative_magnitude_x)
print("Relative Magnitude in Y-direction:", relative_magnitude_y)