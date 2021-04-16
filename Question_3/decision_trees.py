import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt


max_depth = 10     # max depth for the decision tree
test_subset = 0.4  # test subset percentage
depth_range = 50   # depth for decision tree accuracy plot

dataset = pd.read_csv("../data.csv")
dataset.head()

# splitting dataset in features and target variables
feature_columns = ['Roads:number_intersections', 'Roads:diversity', 'Roads:total', 'Buildings:diversity',
                   'Buildings:total', 'LandUse:Mix', 'TrafficPoints:crossing', 'poisAreas:area_park',
                   'poisAreas:area_pitch', 'pois:diversity', 'pois:total', 'ThirdPlaces:oa_count',
                   'ThirdPlaces:edt_count', 'ThirdPlaces:out_count', 'ThirdPlaces:cv_count', 'ThirdPlaces:diversity',
                   'ThirdPlaces:total', 'vertical_density', 'buildings_age', 'buildings_age:diversity']

x = dataset[feature_columns]  # features
y = dataset.most_present_age  # target

# split data into train and test subsets.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_subset, random_state=1) # 70% training subset, 30% test data

# Create Decision Tree Classifier obj
clf = DecisionTreeClassifier(max_depth=max_depth)

# Train Decision Tree Classifier
clf = clf.fit(x_train, y_train)

# Predict response for test dataset.
y_pred = clf.predict(x_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Produce bar chart for feature importance.
fi = clf.feature_importances_
ax = sns.barplot(x=feature_columns, y=fi)
# plt.bar([x for x in feature_columns], fi, color='twilight')
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()

print("\nFeature columns contributions:")
for importance, name in sorted(zip(clf.feature_importances_, feature_columns),reverse=True):
    print (name, importance)

# accuracy score on train and test set
print("\nAccuracy of training set")
print(clf.score(x_train, y_train))
print("\nAccuracy of test set")
print(clf.score(x_test, y_test))

# calculate accuracy for varying depth of the tree and see how it changes
dtc = DecisionTreeClassifier()
scores = []

for dep in range(1, depth_range):

    dtc = DecisionTreeClassifier(max_depth = dep)
    clf = dtc.fit(x_train,y_train)
    scores.append([dep, clf.score(x_test, y_test)])

print("\nAccuracy for varying depths of decision trees")
for i in scores:
    print(i)

plt.title("Accuracy for varying depths of decision trees")
plt.scatter(*zip(*scores))
plt.show()
