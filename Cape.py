import sys
import matplotlib


import pandas as pd
import matplotlib.pyplot as plt
x = list(range(25))
y1 = [0.9, 0.88, 0.87, 0.89, 0.91, 0.92, 0.93, 0.91, 0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.80, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73]
y2 = [0.8, 0.78, 0.76, 0.74, 0.72, 0.70, 0.68, 0.66, 0.64, 0.62, 0.60, 0.58, 0.56, 0.54, 0.52, 0.50, 0.48, 0.46, 0.44, 0.42, 0.40, 0.38, 0.36, 0.34, 0.32]
y3 = [0.7, 0.72, 0.74, 0.76, 0.78, 0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96, 0.98, 1.00, 0.98, 0.96, 0.94, 0.92, 0.90, 0.88, 0.86, 0.84, 0.82]
y4 = [0.6, 0.62, 0.64, 0.66, 0.68, 0.70, 0.72, 0.74, 0.76, 0.78, 0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.88, 0.86, 0.84, 0.82, 0.80, 0.78, 0.76, 0.74, 0.72]

# Plotting the data
plt.plot(x, y1, 'c-', marker='o', label='Line 1')
plt.plot(x, y2, 'm-', marker='o', label='Line 2')
plt.plot(x, y3, 'orange', marker='o', label='Line 3')
plt.plot(x, y4, 'purple', marker='o', label='Line 4')

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('CAPE')
plt.title('CAPE Values Over Time')
plt.legend()

# Display the plot
plt.show()