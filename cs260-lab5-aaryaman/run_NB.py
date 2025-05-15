"""
CS260 Lab 5: Implements read_arff and csv into Partition and then tests NaiveBayes model.
Author: Aaryaman Jaising
Date: Feb 21, 2025
"""
from collections import OrderedDict
import argparse
import sys
import pandas as pd
import numpy as np
from collections import OrderedDict
import random
import NaiveBayes
################################################################################
# CLASSES
################################################################################

class Example:

    def __init__(self, features, label):
        """Helper class (like a struct) that stores info about each example."""
        # dictionary. key=feature name: value=feature value for this example
        self.features = features
        self.label = label # in {0, 1, 2, ..., K-1}

class Partition:

    def __init__(self, data, F, K):
        """Store information about a dataset"""
        # list of Examples
        self.data = data
        self.n = len(self.data)

        # dictionary. key=feature name: value=list of possible values
        self.F = F

        # number of classes
        self.K = K

################################################################################
# MAIN
################################################################################

def main():
    """
    read in the data, run Naive Bayes, make predictions about the test
    data, then print the accuracy and a confusion matrix
    """
    opts = parse_args()
    if opts.train_filename[-3:] == "csv":
        train_partition = read_csv(opts.train_filename)
        test_partition = read_csv(opts.test_filename)
    else:
        train_partition = read_arff(opts.train_filename)
        test_partition = read_arff(opts.test_filename)

    # check
    print("num train =", train_partition.n, ", num classes =", train_partition.K)
    print("num test  =", test_partition.n, ", num classes =", test_partition.K)

    #Code for part 2
    """
    #Training data proportions of male and females
    males = 0
    females = 0
    for example in train_partition.data:
        if example.label == 1:
            females+=1
        else:
            males+=1
    pct_male = 100*males/(males+females)
    print(f"Training Data - Number of Males: {males}, females: {females}, Total = {males+females}")
    print(f"Percentage Males = {pct_male:.2f}%, Females Percentage = {(100-pct_male):.2f}%")
    print()
    
    #Testing with Coin Flip, assuming female is Positive at 1
    TP,TN,FP,FN = 0,0,0,0
    for example in test_partition.data:
        pred = 0 if random.random() <0.5 else 1
        if example.label == 1:
            if pred == 1:
                TP +=1
            else:
                FN +=1
        else:
            if pred == 1:
                FP +=1
            else:
                TN +=1
    print("Using Random Coint to Predict")
    print(f"True Negative: {TN}\tFalse Positive: {FP}")
    print(f"False Negative: {FN}\tTrue Positive: {TP}")
    print(f"Accuracy: {(TP+TN)/(FP+FN+TP+TN)}")
    print()
    #For using majority as prediction where males are majority, so label = 0
    TP,TN,FP,FN = 0,0,0,0
    for example in test_partition.data:
        pred = 0
        if example.label == 1:
            if pred == 1:
                TP +=1
            else:
                FN +=1
        else:
            if pred == 1:
                FP +=1
            else:
                TN +=1
    print("Using Majority to Predict, i.e. all males predicted")
    print(f"True Negative: {TN}\tFalse Positive: {FP}")
    print(f"False Negative: {FN}\tTrue Positive: {TP}")
    print(f"Accuracy: {(TP+TN)/(FP+FN+TP+TN)}")
    print()
    pass
    
    """
    #Code for Part 3 and 4 
    #
    nb = NaiveBayes.NaiveBayes(train_partition)
    
    # Make predictions and evaluate performance
    predictions, accuracy, confusion_matrix = nb.predict(test_partition)

    # Print results
    nb.print_results(accuracy, confusion_matrix)
################################################################################
# HELPER FUNCTIONS
################################################################################

def parse_args():
    """TParse command line arguments (train and test csv or arff files)."""
    parser = argparse.ArgumentParser(prog="run NB",description="Running Naive Bayes model")
    parser.add_argument("-r","--train_filename",type=str,required=True,help="path to train file")
    parser.add_argument("-e","--test_filename",type=str,required=True,help="path to test file")
    return parser.parse_args()
    
    

def read_csv(filename):
    """
    reads the CSV file (from the str filename) into the Partition format.
    """
    df = pd.read_csv(filename)
    F = OrderedDict()
    columns = df.columns
    for c in columns:
        if c != 'sex':
            F[c] = []
    for key in F:
        for value in pd.unique(df[key]):
            F[key].append(value)
    k = len(pd.unique(df['sex']))
    data = []
    for i, row in df.iterrows():
        x_dict = OrderedDict()
        for key in F:
            x_dict[key] = row[key]
        label = 1 if row['sex'] == 'Female' else 0
        data.append(Example(x_dict,label))
    return Partition(data,F,k)

    # return a Partition instance

def read_arff(filename):
    """Read arff file into Partition format."""
    arff_file = open(filename,'r')
    data = [] # list of Examples
    F = OrderedDict() # dictionary
    k=0
    class_set= set()
    header = arff_file.readline()
    line = arff_file.readline().strip()

    # read the attributes
    while line != "@data":
        line = line.replace('{','').replace('}','').replace(',','')
        tokens = line.split()
        name = tokens[1][1:-1]
        features = tokens[2:]

        # label
        if name != "class":
            F[name] = features
        else:
            first = tokens[2]
        line = arff_file.readline().strip()

    # read the examples
    for line in arff_file:
        tokens = line.strip().split(",")
        X_dict = {}
        i = 0
        for key in F:
            val = tokens[i]
            X_dict[key] = val
            i += 1
        label = int(tokens[-1])
        if label not in class_set:
            k+=1
            class_set.add(label)
        data.append(Example(X_dict, label))

    arff_file.close()

    partition = Partition(data, F,k)
    return partition


if __name__ == "__main__":
    main()
