import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generating sample data for scatter plot
x_scatter = np.random.standard_normal(100)
y_scatter = np.random.standard_normal(100)
z_scatter = np.random.standard_normal(100)

# Generating data for surface plot
x_surface = np.linspace(-5, 5, 50)
y_surface = np.linspace(-5, 5, 50)
x_surface, y_surface = np.meshgrid(x_surface, y_surface)
z_surface = np.sin(np.sqrt(x_surface**2 + y_surface**2))

# Creating the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adding scatter plot
ax.scatter(x_scatter, y_scatter, z_scatter, color='b')

# Adding surface plot
ax.plot_surface(x_surface, y_surface, z_surface, cmap='viridis', alpha=0.6)

# Setting labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Show plot
plt.show()
