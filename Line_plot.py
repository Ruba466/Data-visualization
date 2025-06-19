import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 11]

# Create the plot
plt.plot(x, y, color='blue', marker='o', linestyle='--')

plt.title("Simple Line Plot Example")
plt.xlabel("X-axis (Time)")
plt.ylabel("Y-axis (Value)")


plt.grid(True)

# save image
plt.savefig('Images/line_plot.png')

# Show the plot
plt.show()
