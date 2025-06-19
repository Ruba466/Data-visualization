import matplotlib.pyplot as plt

# Sample data
subjects = ['Math', 'Science', 'English', 'History', 'Art']
scores = [85, 90, 78, 88, 76]
colors = ['red', 'green', 'blue', 'orange', 'purple']

# Create the bar chart
plt.bar(subjects, scores, color=colors)

# Add title and labels
plt.title("Student Scores by Subject")
plt.xlabel("Subjects")
plt.ylabel("Scores")

# save image 
plt.savefig('Images/bar_chart.png')

# Show the plot
plt.show()
