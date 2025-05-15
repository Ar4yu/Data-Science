"""
Author: Aaryaman Jaising
Date: Tuesday, March 25th, 2025
"""
#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt
from LogisticRegression import LogisticRegression
from LogisticRegression import plot_challenger

def load_data(filename):
    """
    Loads a CSV file and returns features and labels using np.loadtxt.
    Assumes that the file does not have a header and that the last column is the label.
    
    Parameters
    ----------
    filename : str
        Path to the CSV file.
        
    Returns
    -------
    X : numpy.ndarray
        Feature matrix with all columns except the last.
    y : numpy.ndarray
        Labels array with the last column of the file.
    """
    data = np.loadtxt(filename, delimiter=',')
    # Ensure data is 2D even if the file contains only one row.
    data = np.atleast_2d(data)
    X = data[:, :-1]
    y = data[:, -1]
    return X, y


def evaluate_predictions(y_true, y_pred):
    """
    Compute accuracy and confusion matrix.
    
    Returns:
        accuracy: float
        confusion_matrix: 2x2 numpy array in the format:
                          [[TN, FP],
                           [FN, TP]]
    """
    TN = np.sum((y_pred == 0) & (y_true == 0))
    FP = np.sum((y_pred == 1) & (y_true == 0))
    FN = np.sum((y_pred == 0) & (y_true == 1))
    TP = np.sum((y_pred == 1) & (y_true == 1))
    accuracy = (TN + TP) / len(y_true)
    confusion_matrix = np.array([[TN, FP], [FN, TP]])
    return accuracy, confusion_matrix


def main():
    # Parse command-line arguments.
    parser = argparse.ArgumentParser(description="Logistic Regression Implementation")
    parser.add_argument("-r", "--train", required=True, help="Path to training data CSV file")
    parser.add_argument("-e", "--test", required=True, help="Path to test data CSV file")
    parser.add_argument("-a", "--alpha", required=True, type=float, help="Learning rate")
    args = parser.parse_args()

    # Load training and test data
    X_train, y_train = load_data(args.train)
    X_test, y_test = load_data(args.test)

    # Initialize and train the logistic regression model.
    # The LogisticRegression class (from LogisticRegression.py) automatically adds the bias term.
    #ideal is 0.05
    model = LogisticRegression(alpha=args.alpha,tol=0.00001,max_iter=100000)
    model.fit(X_train, y_train)

    # Predict on the test set.
    y_pred = model.predict(X_test)

    # Evaluate accuracy and compute confusion matrix.
    accuracy, confusion_matrix = evaluate_predictions(y_test, y_pred)
    print("Accuracy: {:.6f}".format(accuracy))
    print(f"{confusion_matrix[0,0]+confusion_matrix[1,1]} out of {sum(sum(confusion_matrix))} correct")
    print("Confusion Matrix:")
    print("   prediction")
    print("      0   1")
    print("    ------")
    print("0 | {}   {}".format(confusion_matrix[0, 0], confusion_matrix[0, 1]))
    print("1 | {}   {}".format(confusion_matrix[1, 0], confusion_matrix[1, 1]))

    # If the training file is for the Challenger dataset, generate visualization.
    if "challenger" in args.train.lower():
        plot_challenger(X_train, y_train, X_test, y_test, model, filename="output/challenger.pdf")
        prob = model.predict_proba(X_test)
        print("Probability Challenger Exploded was: ", prob)

if __name__ == "__main__":
    main()
