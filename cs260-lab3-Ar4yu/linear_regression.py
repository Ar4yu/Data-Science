"""
Linear Regression and Gradient Descent
Author: Aaryaman Jaising
Date: Feb 4, 2025
"""

# python libraries import here
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

################################################################################
# MAIN
################################################################################

def main() :
    args = parse_arguments()
    filename = args.data_filename
    data = pd.read_csv(filename,header=None)
    print(data.head())
    #Steps for sea ice data
    # x = np.array(data[0])
    # y = np.array(data[1])
    # w = fit(x,y)
    # print(w)
    # for the sea_ice dataset its values are [ 1.90503821e+02 -9.22444604e-02]

    X = data.iloc[:, :-1].values  # Features: columns 0 to 4
    y = data.iloc[:, -1].values   # Target: Price (column 5)
    
    # Normalize the features (each column separately)
    X_mean = np.mean(X, axis=0)
    X_std = np.std(X, axis=0)
    X_normalized = (X - X_mean) / X_std
    
    # Optionally, normalize the target as well (this is useful when using gradient descent)
    y_mean = np.mean(y)
    y_std = np.std(y)
    y_normalized = (y - y_mean) / y_std

    w = fit(X_normalized, y_normalized)
    print("\nComputed weights (analytic solution):")
    print(w)
    
    # Compute the cost on normalized data
    cost_val = cost(X_normalized, y_normalized, w)
    print("\nCost (normalized data):", cost_val)
    #For the USA housing data
    # Computed weights (analytic solution):
    # [8.03820875e-17 6.51280605e-01 4.65062749e-01 3.43692235e-01
    #  5.77068966e-03 4.27271975e-01]

    # Cost (normalized data): 204.94045122011386

    #using fit_sgd
    w_sgd = fit_SGD(X_normalized,y_normalized,alpha=0.00001)


################################################################################
# HELPER FUNCTIONS
################################################################################
def add_ones(x):
    """
    This function adds a column of 1's to the give numpy array, also handles reshaping
    x: input data array
    """
    if x.ndim == 1:
        x = x.reshape(-1, 1)
    ones = np.ones((x.shape[0],1))
    return np.concatenate((ones,x),axis=1)

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(prog="Linear Regression",
                                     description='run linear regression method')

    parser.add_argument('-d', '--data_filename', type=str, required=True,
                        help='path to CSV file of data')

    return parser.parse_args()

def fit(X, y) :
    """
    Closed-form solution.
    X: given x values in a matrix,
    y: given output values for dataset in a numpy array
    uses closed form solution to calculate and return weights
    
    """
    X1 = add_ones(X)
    x_transpose = np.transpose(X1)
    xtx = np.matmul(x_transpose,X1)
    xty = np.matmul(x_transpose,y)
    xtx_inverse = np.linalg.pinv(xtx)
    weights = np.matmul(xtx_inverse,xty)
    return weights

def fit_SGD(X, y, alpha, eps=1e-10, tmax=10000):
    """
    SGD solution.
    X: input data
    y: output data
    alpha: step size, int
    eps: criteria for convergence
    tmax: max iteration stops if it diverges.

    Uses stochastic gradient descent and returns weights
    """
    print("\nSGD")
    x = add_ones(X)
    w = np.zeros((x.shape[1],1))
    iterations = 0
    costs = []
    costs.append(cost(X,y,w))
    for n in range(tmax):
        w_old = w.copy()
        for i in range(y.shape[0]):
            x_i = x[i].reshape(-1,1)
            y_hat = np.matmul(x_i.T,w)
            error = y_hat - y[i]
            gradient = error*x_i
            w = w - alpha*gradient
        costs.append(cost(X,y,w))
        if abs(cost(X,y,w)-cost(X,y,w_old)) < eps:
            print("Converged at step #",n)
            print("SGD Weights calculated are: ",w)
            print("SGD cost at current weight is: ",cost(X,y,w))
            print(f"Relevant values are: Alpha - {alpha}, epsilon - {eps}, and max steps - {tmax}")
            w_analytical = fit(X,y)
            print("Analytic Solution has weight: ",w_analytical)
            print("Analytic Solution has cost: ",cost(X,y,w_analytical))
            plt.plot(range(len(costs)),costs)
            plt.xlabel("Iteration")
            plt.ylabel("Cost")
            plt.title("SGD Analysis of Costs along descent")
            plt.savefig("figures/cost_J.pdf",format = "pdf")
            return w
        

    print("Did not converge, reached max: ", tmax)
    print("SGD Weights calculated are: ",w)
    print("SGD cost at current weight is: ",cost(X,y,w))
    print(f"Relevant values are: Alpha - {alpha}, epsilon - {eps}, and max steps - {tmax}")
    w_analytical = fit(X,y)
    print("Analytic Solution has weight: ",w)
    print("Analytic Solution has cost: ",cost(X,y,w_analytical))
    return w



    pass

def predict(X, w) :
    """
    Predict output for X using weight vector w.
    X: input data
    w: weights
    returns predicted data
    """
    X_mod = add_ones(X)
    return np.matmul(X_mod,w)

def cost(X, y, w):
    """
    Calculate the loss/cost function (sum of squared errors divided by 2).
    Returns a scalar.x
    """
    y_hat = predict(X, w).flatten()#was having issues with dimensionality
    return 0.5 * np.sum((y - y_hat) ** 2)

if __name__ == "__main__" :
    main()
