"""
PCA analysis using sklearn library for Iris dataset
Author: Aaryaman Jaising
Date: April 3rd, 2025
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn import decomposition
from sklearn import datasets

def main():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    print("X.shape = ", X.shape)
    #X.shape =  (150, 4)
    #print(X[:5,:])

    #print(Y)

    pca = decomposition.PCA(n_components=2)
    pca.fit(X)
    x_transform = pca.fit_transform(X)
    color_dict = {0:'c',1:"m",2:"y"}
    colors = [color_dict[label] for label in Y]

    plt.scatter(x_transform[:,0],x_transform[:,1],c = colors)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("PCA Analysis for Iris Dataset")
    leg_objects = []
    names = ["Iris Setosa","Iris Versicolour","Iris Virginica"]
    for i in range(3):
        circle, = plt.plot([], 'o', c=color_dict[i])
        leg_objects.append(circle)
    plt.legend(leg_objects,names)

    plt.savefig("figures/iris.pdf")

    #wine dataset
    wine = datasets.load_wine()
    X_wine = wine.data
    y_wine = wine.target
    
    pca_wine = decomposition.PCA(n_components=2)
    X_wine_trans = pca_wine.fit_transform(X_wine)
    
    color_dict = {0: 'c', 1: 'm', 2: 'y'}
    wine_class_names = wine.target_names.tolist()
    colors = [color_dict[label] for label in y_wine]
    #plotting
    plt.scatter(X_wine_trans[:,0],X_wine_trans[:,1],c = colors)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("PCA Analysis for Wine Dataset")
    leg_objects = []
    for i in range(3):
        circle, = plt.plot([], 'o', c=color_dict[i])
        leg_objects.append(circle)
    plt.legend(leg_objects,wine_class_names)

    plt.savefig("figures/other_pca.pdf")


if __name__ == "__main__":
    main()