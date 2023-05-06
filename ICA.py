import numpy as np
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt

# generate a sample dataset
np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)
s1 = np.sin(2 * time)  # Signal 1 : sinusoidal signal
s2 = np.sign(np.sin(3 * time))  # Signal 2 : square signal
s3 = np.random.randn(n_samples)  # Signal 3 : noise
S = np.c_[s1, s2, s3]
S /= S.std(axis=0)  # Standardize data
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Mixing matrix
X = np.dot(S, A.T)  # Generate observations

# Compute ICA
ica = FastICA(n_components=3)
S_ = ica.fit_transform(X)  # Get the estimated sources
A_ = ica.mixing_  # Get estimated mixing matrix

# Plot the original sources and the estimated sources
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(S)
plt.title('Original Sources')
plt.subplot(3, 1, 2)
plt.plot(S_)
plt.title('ICA Estimated Sources')
plt.subplot(3, 1, 3)
plt.plot(X)
plt.title('Observations (mixed signal)')
plt.tight_layout()
plt.show()
