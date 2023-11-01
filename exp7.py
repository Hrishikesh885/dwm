import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import numpy as np

# Data points
#data = [18, 22, 25, 42, 27, 43]
data=input("Enter data:- ").split()
data=[int(d) for d in data]
# Perform agglomerative clustering
data_array = np.array(data).reshape(-1, 1)
Z = linkage(data_array, method='ward')

# Function to plot a dendrogram
def plot_dendrogram(linkage_matrix, labels):
    plt.figure()
    plt.title("Dendrogram")

    dendrogram(linkage_matrix, orientation="top", labels=labels, distance_sort='descending')
    plt.xlabel("Clusters")
    plt.ylabel("Distance")
    plt.show()

# Create labels for the data points
labels = [str(x) for x in data]

# Plot the dendrogram
plot_dendrogram(Z, labels)

# Function to generate and display the distance matrix
def display_distance_matrix(Z, data):
    num_steps = len(Z)
    num_data = len(data)
    distance_matrices = []

    for i in range(num_steps + 1):
        clusters = fcluster(Z, i + 1, criterion='maxclust')
        distance_matrix = np.zeros((num_data, num_data))

        for j in range(num_data):
            for k in range(num_data):
                if clusters[j] != clusters[k]:
                    distance_matrix[j, k] = distance_matrix[k, j] = abs(data[j] - data[k])

        distance_matrices.insert(0, distance_matrix)  # Insert at the beginning to keep them in order.

    return distance_matrices

# Display distance matrices at each step
distance_matrices = display_distance_matrix(Z, data)
for i, matrix in enumerate(distance_matrices):
    print(f"Step {i} - Distance Matrix:")
    print(matrix)
    print()
