"""
Use entropy to find the best feature in a training dataset.
Author: Sara Mathieson
Date: 3/17/25
"""

# python imports
import sys
import argparse
# my file imports
from Partition import *

################################################################################
# MAIN
################################################################################

def main():
    #Added code for reading in files and finding best features.
    opts = parse_args()
    train_partition = read_arff(opts.train_filename)
    best_f = train_partition.best_feature()
    print("best feature by information gain:", best_f)
    best_feature_accuracy = train_partition.best_feature_by_accuracy()
    print(f"Best Feature by accuracy: {best_feature_accuracy}")

    pass

################################################################################
# HELPER FUNCTIONS
################################################################################

def parse_args():
    # Parses arguments from command line
    parser = argparse.ArgumentParser(prog="best_feature.py",description="Finding the best features using information Gain")
    parser.add_argument("-r","--train_filename",type=str,required=True,help="path to arff file")
    
    return parser.parse_args()

def read_arff(filename):
    """
    Read arff file into Partition format. Params:
    * filename (str), the path to the arff file
    """
    arff_file = open(filename,'r')
    data = [] # list of Examples
    F = {} # key: feature name, value: list of feature values

    header = arff_file.readline()
    line = arff_file.readline().strip()

    # read the attributes
    while line != "@data":

        clean = line.replace('{','').replace('}','').replace(',','')
        tokens = clean.split()
        name = tokens[1][1:-1]

        # discrete vs. continuous feature
        if '{' in line:
            feature_values = tokens[2:]
        else:
            feature_values = "cont"

        # record features or label
        if name != "class":
            F[name] = feature_values
        else:
            # first will be label -1, second will be +1
            first = tokens[2]
        line = arff_file.readline().strip()

    # read the examples
    for line in arff_file:
        tokens = line.strip().split(",")
        X_dict = {}
        i = 0
        for key in F:
            val = tokens[i]
            if F[key] == "cont":
                val = float(tokens[i])
            X_dict[key] = val
            i += 1

        # change binary labels to {-1, 1}
        label = -1 if tokens[-1] == first else 1
        # add to list of Examples
        data.append(Example(X_dict,label))

    arff_file.close()

    # convert continuous features to discrete
    F_disc = {}
    for feature in F:

        # if continuous, convert feature (NOTE: modifies data and F_disc)
        if F[feature] == "cont":
            convert_one(feature, data, F_disc)

        # if not continuous, just copy over
        else:
            F_disc[feature] = F[feature]

    partition = Partition(data, F_disc)
    return partition

def convert_one(f, data, F_disc):
    """
    Convert one feature (name f) from continuous to discrete.
    Credit: based on original code from Ameet Soni.
    """

    # first combine the feature values (for f) and the labels
    combineXy = []
    for example in data:
        combineXy.append([example.features[f],example.label])
    combineXy.sort(key=lambda elem: elem[0]) # sort by feature

    # first need to merge uniques
    unique = []
    u_label = {}
    for elem in combineXy:
        if elem[0] not in unique:
            unique.append(elem[0])
            u_label[elem[0]] = elem[1]
        else:
            if u_label[elem[0]] != elem[1]:
                u_label[elem[0]] = None

    # find switch points (label changes)
    switch_points = []
    for j in range(len(unique)-1):
        if u_label[unique[j]] != u_label[unique[j+1]] or u_label[unique[j]] \
            == None:
            switch_points.append((unique[j]+unique[j+1])/2) # midpoint

    # add a feature for each switch point (keep feature vals as strings)
    for s in switch_points:
        key = f+"<="+str(s)
        for i in range(len(data)):
            if data[i].features[f] <= s:
                data[i].features[key] = "True"
            else:
                data[i].features[key] = "False"
        F_disc[key] = ["False", "True"]

    # delete this feature from all the examples
    for example in data:
        del example.features[f]

if __name__ == "__main__":
    main()
