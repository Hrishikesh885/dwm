import matplotlib.pyplot as plt

# Sample data (replace with your own data)
data = [2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

# Create a histogram
plt.hist(data, bins=5, color='blue', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Show the histogram
plt.show()
