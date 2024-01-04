from sklearn.datasets import load_iris
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris=load_iris()
print("IRIS:",iris.data)
print("IRIS FEATURES:",iris.feature_names)
print("IRIS TARGET:",iris.target)
print("IRIS TARGET NAMES:",iris.target_names)

for i in range(len(iris["target_names"])):
    print("\n [{0}]:[{1}]".format(i,iris["target_names"][i]))

X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target,random_state=0)

# KNN
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

# x=np.array([5.2,4.0,1.8,0.1])
# prediction=knn.predict([x])
# print("Predicted:[{0}] Name:[{1}]".format(prediction,iris.target_names[prediction]))

for i in range(len(X_test)):
    x=X_test[i]
    prediction=knn.predict([x])
    print("Actual [{0}]: [{1}] Predicted [{2}]:[{3}]".format(y_test[i],iris.target_names[y_test[i]],prediction,iris["target_names"][prediction]))
print("Score:{:.2f}".format(knn.score(X_test,y_test)))
