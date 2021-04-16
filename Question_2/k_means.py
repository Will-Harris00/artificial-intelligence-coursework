# Standard scientific Python imports
import numpy as np
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

digits, target = load_digits(return_X_y=True)
dataset = digits.data

samples_count, features_count = dataset.shape
digits_count = np.unique(target).size
print("Number of unique digits:",digits_count,
      "\nNumber of samples:",samples_count,
      "\nNumber of features:",features_count)


reduced_data = PCA(n_components=2).fit_transform(dataset)
kmeans = KMeans(init="k-means++", n_clusters=digits_count, n_init=10, random_state=0)
kmeans.fit(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
quality = .05     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 10, reduced_data[:, 0].max() + 10
y_min, y_max = reduced_data[:, 1].min() - 10, reduced_data[:, 1].max() + 10
xx, yy = np.meshgrid(np.arange(x_min, x_max, quality), np.arange(y_min, y_max, quality))

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.clf()
plt.imshow(Z, interpolation="nearest",
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap='RdBu', aspect="auto", origin="lower")

# Plot the centroids as a white X
centroids = kmeans.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=150,
            color='w', zorder=10, label=0)

colours = ['crimson', 'purple', 'indigo', 'darkturquoise', 'goldenrod', 'orangered',
          'mediumvioletred', 'darkorange', 'mediumorchid', 'tan']
for i in range(0,10):
    x = reduced_data[:, 0][target == i]
    y = reduced_data[:, 1][target == i]
    plt.scatter(x, y, c=colours[i], s=10, label=colours[i])
    plt.legend(target, bbox_to_anchor=(1,1), loc=2, borderaxespad=0)

plt.title("K-means clustering on the digits dataset (PCA-reduced data)\n"
          "Centroids are marked with white cross")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
