import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
dataset = digits.data

_, axes = plt.subplots(nrows=2, ncols=5)
for ax, image, label in zip(axes.flat, digits.images, digits.target):
    ax.set(xticks=[], yticks=[])
    ax.imshow(image, cmap='binary', interpolation='nearest')
    ax.set_title('Number: %i' % label)

plt.show()
