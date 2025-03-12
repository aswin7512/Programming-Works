import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def knn_sampling_with_outlier_removal(X, k):
  """Performs k-NN sampling with outlier removal.

  Args:
    X: A numpy array containing the data to sample from.
    k: The number of neighbors to consider.

  Returns:
    A numpy array containing the sampled data.
  """

  # Create a KNeighborsClassifier object.
  knn = KNeighborsClassifier(n_neighbors=k)

  # Fit the KNeighborsClassifier object to the data.
  knn.fit(X, np.zeros(X.shape[0]))

  # Get the neighbors of each data point.
  neighbors = knn.kneighbors(X, return_distance=False)

  # Calculate the average distance to the neighbors.
  avg_distances = np.mean(neighbors, axis=1)

  # Identify outliers as data points with an average distance to their neighbors
  # that is greater than a threshold.
  threshold = 2 * np.median(avg_distances)
  outliers = np.where(avg_distances > threshold)[0]

  # Remove outliers from the data.
  X_clean = np.delete(X, outliers, axis=0)

  # Sample the data using k-NN.
  sample = knn.kneighbors(X_clean, return_distance=False)[1][:, 0]

  return sample

# Example usage:

X = np.loadtxt("data.csv", delimiter=",")

# Sample the data using k-NN with outlier removal.
sample = knn_sampling_with_outlier_removal(X, k=10)

# Use the sampled data to create the initial visual environment for LION-tSNE.

