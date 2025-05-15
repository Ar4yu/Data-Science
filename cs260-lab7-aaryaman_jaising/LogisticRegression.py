"""
Object Oriented Implementation of Logistic Regression
Author: Aaryaman Jaising
Date: Tuesday, March 25th, 2025
"""

import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:
    """
    Logistic Regression (aka logit, MaxEnt) classifier.

    Parameters
    ----------
    alpha: float, default=0.01
        Learning rate
    tol : float, default=0.0001
        Tolerance for stopping criteria (difference in loss)
    max_iter : int, default=10000
        Maximum number of epochs of gradient descent
    theta_init: None (or) numpy.ndarray of shape (D + 1,)
        The initial weights; if None, all weights will be zero by default

    Attributes
    ----------
    theta_ : numpy.ndarray of shape (D + 1,)
        The value of the coefficients after gradient descent has converged
        or the number of epochs hit the maximum limit
    hist_theta_ : numpy.ndarray of shape (num_epoch, D + 1) where num_epoch is the number of epochs
        Stores theta_ after every gradient descent epoch
    hist_cost_ : numpy.ndarray of shape (num_epoch,) where num_epoch is the number of epochs
        Stores cost after every gradient descent epoch
    """

    def __init__(self, alpha=0.01, tol=0.0001, max_iter=10000, theta_init=None):
        self.alpha = alpha
        self.tol = tol
        self.max_iter = max_iter
        self.theta_init = theta_init
        self.theta_ = None
        self.hist_cost_ = None
        self.hist_theta_ = None

    def sigmoid(self, x):
        """
        Compute the sigmoid value of the argument.

        Parameters
        ----------
        x: numpy.ndarray

        Returns
        -------
        out: numpy.ndarray
            The sigmoid value of x
        """
        return 1 / (1 + np.exp(-x))

    def compute_cost(self, theta, X, y):
        """
        Compute the cost/objective function.

        Parameters
        ----------
        theta: numpy.ndarray of shape (D + 1,)
            The coefficients
        X: numpy.ndarray of shape (N, D + 1)
            The features matrix
        y: numpy.ndarray of shape (N,)
            The target variable array

        Returns
        -------
        cost: float
            The cost as a scalar value
        """
        h = self.sigmoid(np.dot(X, theta))
        # Compute cost without regularization
        cost = -np.nansum(y * np.log(h) + (1 - y) * np.log(1 - h))
        return cost

    def compute_gradient(self, theta, X, y):
        """
        Compute the gradient of the cost function for the full dataset.

        Parameters
        ----------
        theta: numpy.ndarray of shape (D + 1,)
            The coefficients
        X: numpy.ndarray of shape (N, D + 1)
            The features matrix
        y: numpy.ndarray of shape (N,)
            The target variable array

        Returns
        -------
        gradient: numpy.ndarray of shape (D + 1,)
            The gradient values
        """
        z = np.nansum(np.multiply(X, theta), axis=1)
        h = self.sigmoid(z)
        error = h - y  # shape (N,)
        grad = np.nansum(np.multiply(X, error[:, np.newaxis]), axis=0)
        return grad

    def has_converged(self, cost_old, cost_new):
        """
        Return whether gradient descent has converged based on the change in loss.

        Parameters
        ----------
        cost_old: float
            The cost before the weight update
        cost_new: float
            The cost after the weight update

        Returns
        -------
        converged: bool
            Whether gradient descent converged or not
        """
        return abs(cost_new - cost_old) <= self.tol

    def fit(self, X, y):
        """
        Compute the coefficients using stochastic gradient descent and store them as theta_.
        At each epoch, the training examples are shuffled and the weights are updated one at a time.

        Parameters
        ----------
        X: numpy.ndarray of shape (N, D)
            The features matrix
        y: numpy.ndarray of shape (N,)
            The target variable array

        Returns
        -------
        Nothing
        """
        N, D = X.shape
        # Add bias term: column of ones
        ones_col = np.ones((N, 1))
        X = np.hstack((ones_col, X))

        # Initialize the weights
        if self.theta_init is None:
            theta = np.zeros((D + 1,))
        else:
            theta = self.theta_init

        # Initialize historical weights and cost
        self.hist_theta_ = np.array([theta])
        cost_old = self.compute_cost(theta, X, y)
        self.hist_cost_ = np.array([cost_old])

        # Stochastic Gradient Descent
        for epoch in range(self.max_iter):
            # Shuffle training examples
            indices = np.random.permutation(N)
            for i in indices:
                xi = X[i]
                yi = y[i]
                prediction = self.sigmoid(np.dot(xi, theta))
                # Compute gradient for this single example
                grad_i = (prediction - yi) * xi
                # Update theta using this example
                theta = theta - self.alpha * grad_i

            # Compute cost over the full dataset after processing all examples in the epoch
            cost_new = self.compute_cost(theta, X, y)
            self.hist_theta_ = np.vstack((self.hist_theta_, theta))
            self.hist_cost_ = np.append(self.hist_cost_, cost_new)
            if self.has_converged(cost_old, cost_new):
                break
            cost_old = cost_new

        self.theta_ = theta

    def predict_proba(self, X):
        """
        Predict the probabilities that the data points in X belong to class 1.

        Parameters
        ----------
        X: numpy.ndarray of shape (N, D)
            The features matrix

        Returns
        -------
        y_hat: numpy.ndarray of shape (N,)
            The predicted probabilities that the data points in X belong to class 1
        """
        N = X.shape[0]
        X = np.hstack((np.ones((N, 1)), X))
        y_hat = self.sigmoid(np.dot(X, self.theta_))
        return y_hat

    def predict(self, X):
        """
        Predict the classes of the data points in X.

        Parameters
        ----------
        X: numpy.ndarray of shape (N, D)
            The features matrix

        Returns
        -------
        y_pred: numpy.ndarray of shape (N,)
            The predicted class (0 or 1) for the data points in X
        """
        y_pred = np.where(self.predict_proba(X) >= 0.5, 1, 0)
        return y_pred

def plot_challenger(X_train, y_train, X_test, y_test, model, filename="challenger.pdf"):
    """
    Visualize the Challenger dataset with improved scaling and display
    """
    plt.figure(figsize=(10, 6))
    
    # Create prediction line with more points
    x_min = min(X_train[:,0].min(), X_test[:,0].min()) - 5
    x_max = max(X_train[:,0].max(), X_test[:,0].max()) + 5
    x_vals = np.linspace(x_min, x_max, 500).reshape(-1, 1)
    y_probs = model.predict_proba(x_vals)
    
    # Plot training data (failures and successes)
    plt.scatter(X_train[y_train==0, 0], y_train[y_train==0], 
                c='blue', marker='o', label='Train: No Failure', alpha=0.7)
    plt.scatter(X_train[y_train==1, 0], y_train[y_train==1], 
                c='red', marker='x', label='Train: Failure', s=100, linewidths=2)
    
    # Plot test point
    plt.scatter(X_test[:, 0], y_test, 
                c='green', marker='*', s=200, label='Test Point (Challenger)', linewidths=2)
    
    # Plot logistic curve
    plt.plot(x_vals, y_probs, 'k-', linewidth=2, label='Model Probability')
    
    # Add decision boundary at 0.5
    plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    
    # Calculate and display accuracy if we have multiple test points
    if len(y_test) > 1:
        y_pred = model.predict(X_test)
        correct = sum(y_pred == y_test)
        total = len(y_test)
        acc = correct/total
        plt.text(0.02, 0.95, f'Accuracy: {acc:.1%} ({correct} out of {total})',
                 transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8))
    
    # Formatting
    plt.xlabel('Temperature (°F)', fontsize=12)
    plt.ylabel('Failure Probability', fontsize=12)
    plt.title('O-Ring Failure Probability vs Temperature', fontsize=14)
    plt.legend(loc='upper right', framealpha=1)
    plt.grid(True, alpha=0.3)
    plt.ylim(-0.1, 1.1)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()