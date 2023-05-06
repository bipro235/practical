import numpy as np

from sklearn.cluster import SpectralClustering

# generate a sample dataset
X = np.array([[1,2],[1,1],[1,2],[2,2],[4,4],[4,5],[5,4],[5,5]])

# Create the spectral clustering object with two cluster
sc = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', n_neighbors = 4)

# Fit the model to the data and predict the cluster labels
labels = sc.fit_predict(X)

print(labels)

