import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
dataset = digits.data

_, axes = plt.subplots(nrows=2, ncols=5)
for ax, image, label in zip(axes.flat, digits.images, digits.target):
    ax.set(xticks=[], yticks=[])
    ax.imshow(image, cmap='binary', interpolation='nearest')
    ax.set_title('Number: %i' % label)
plt.suptitle("Visual representation of all ten digits" )
plt.show()

_, axes = plt.subplots(6, 6, figsize=(12, 12))
for ax, image, label in zip(axes.flat, digits.images, digits.target):
    ax.imshow(image, cmap='binary')
    ax.set(xticks=[], yticks=[])
    ax.set_title(label)
plt.suptitle("Image samples shown with their true target label", fontsize=25)

plt.show()
