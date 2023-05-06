import numpy as np
from sklearn.cluster import KMeans

#Generate the sample data
X = np.array([[1,2],[1.5,1.8], [5,8], [8,8], [1,0.6], [9,11]])

# Create a clustering object with 2 clusters 
km = KMeans(n_clusters=2)

# fit the model to the data
km.fit(X)

#Get the clusters label for each data points
labels = km.labels_

#Get the center for each clusters
center = km.cluster_centers_

#Print the cluster and the center
print(labels)
print(center)