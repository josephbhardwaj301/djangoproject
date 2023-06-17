import matplotlib.pyplot as plt
import numpy as np
# Multiple  plots
# Generate some data for the plot
x = np.linspace(0, 10, 100)  # Create an array of 100 evenly spaced points between 0 and 10
y_sin = np.sin(x)  # Calculate the sine of each x value
y_cos = np.cos(x)  # Calculate the cosine of each x value

# Create a new figure and Axes object
fig, ax = plt.subplots()

# Plot the sine and cosine waves with different colors and labels
ax.plot(x, y_sin, color='red', linestyle='-', linewidth=2, label='Sine')
ax.plot(x, y_cos, color='blue', linestyle='--', linewidth=2, label='Cosine')

# Set the title, x-axis label, and y-axis label
ax.set_title('Sine and Cosine Waves')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add gridlines to the plot
ax.grid(True, linestyle='--', color='gray', alpha=0.5)

# Customize the tick labels and locations
ax.set_xticks(np.linspace(0, 10, 11))
ax.set_xticklabels(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
ax.set_yticks(np.linspace(-1, 1, 11))
ax.tick_params(axis='both', labelsize=10)

# Add a legend to the plot
ax.legend(loc='upper right')

# Customize the spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_position(('outward', 10))

# Display the plot
plt.show()