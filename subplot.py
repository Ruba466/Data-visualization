import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 11]
labels = [f'Item {i}' for i in x]

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Line Plot
axs[0].plot(x, y, color='blue', marker='*', linestyle='--')
axs[0].set_title("Line Plot")
axs[0].set_xlabel("X-axis (Time)")
axs[0].set_ylabel("Y-axis (Value)")
axs[0].grid(True)

# Bar Chart
axs[1].bar(x, y, color='green')
axs[1].set_title("Bar Chart")
axs[1].set_xlabel("X-axis (Time)")
axs[1].set_ylabel("Y-axis (Value)")
axs[1].grid(True)

# Pie Chart (using y values as portions, and x as labels)
axs[2].pie(y, labels=labels, autopct='%1.1f%%', startangle=90)
axs[2].set_title("Pie Chart")

# Adjust layout
plt.tight_layout()

# Save the full figure
plt.savefig('Images/subplots_combined.png')

# Show all plots
plt.show()
