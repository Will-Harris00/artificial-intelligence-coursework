# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

digits = datasets.load_digits()

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
clf = svm.SVC(gamma=0.001)

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False)

# Learn the digits on the train subset
clf.fit(X_train, y_train)

# Predict the value of the digit on the test subset
predicted = clf.predict(X_test)

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, X_test, predicted):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.binary, interpolation='nearest')
    ax.set_title(f'Prediction: {prediction}')
plt.suptitle("Visualisation of image samples shown with their predicted digit value")
plt.show()

disp = metrics.plot_confusion_matrix(clf, X_test, y_test, cmap='cubehelix')
# we are only using half the dataset for testing so we index the latter half
plt.title("Confusion Matrix showing prediction accuracy of " +
                  str(round(accuracy_score(digits.target[898:], predicted), 2) * 100) + "%")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()
