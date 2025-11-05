import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("A Simple Sine Wave")
plt.show()





# Create a figure and an axes
fig, ax = plt.subplots()
# ax is Axes
fig

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot takes place using the data on the axes
ax.plot(x, y)

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('A Simple Sine Wave')
