from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import sklearn.metrics as sm

l1=[0,1,2]
def rename(s):
    l2=[]
    for i in s:
        if i not in l2:
            l2.append(i)
    for i in range(len(s)):
        pos=l2.index(s[i])
        s[i]=l1[pos]

    return s

iris=datasets.load_iris()
print("IRIS:",iris.data)
print("IRIS FEATURES:",iris.feature_names)
print("IRIS TARGET:",iris.target)
print("IRIS TARGET NAMES:",iris.target_names)

X=pd.DataFrame(iris.data)
X.columns=["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width"]

y=pd.DataFrame(iris.target)
y.columns=["Target"]
colormap=np.array(["red","lime","black"])

# KMeans Algorithm
kmm=KMeans(n_clusters=3)
kmm.fit(X)

k_labels=rename(kmm.labels_)

# plot Real vs KMeans
plt.figure(figsize=(14,7))

plt.subplot(1,2,1)
plt.scatter(X.Sepal_Length,X.Sepal_Width,c=colormap[y.Target],s=40)
plt.title("Real Classification")

plt.subplot(1,2,2)
plt.scatter(X.Sepal_Length,X.Sepal_Width,c=colormap[k_labels],s=40)
plt.title("KMeans Classification")
plt.show()

# Metrics of KMeans
print("What KMeans thought:",k_labels)
print("Accuracy Score:",sm.accuracy_score(y.Target,k_labels))
print("Confusion Matrix:",sm.confusion_matrix(y.Target,k_labels))

# Preprocessing

from sklearn import preprocessing

scaler=preprocessing.StandardScaler()
scaler.fit(X)
xsa=scaler.transform(X)
xs=pd.DataFrame(xsa,columns=X.columns)

gmm=GaussianMixture(n_components=3)
gmm.fit(xs)

values=gmm.predict(xs)
g_labels=rename(values)

# plot Real vs EM
plt.figure(figsize=(14,7))

plt.subplot(1,2,1)
plt.scatter(X.Sepal_Length,X.Sepal_Width,c=colormap[y.Target],s=40)
plt.title("Real Classification")

plt.subplot(1,2,2)
plt.scatter(X.Sepal_Length,X.Sepal_Width,c=colormap[g_labels],s=40)
plt.title("EM Algorithm")
plt.show()

# Metrics of EM
print("What EM thought:",g_labels)
print("Accuracy Score:",sm.accuracy_score(y.Target,g_labels))
print("Confusion Matrix:",sm.confusion_matrix(y.Target,g_labels))








