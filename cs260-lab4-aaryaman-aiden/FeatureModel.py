"""
Feature Model main program  
Author: Aaryman Jaising and Aiden Kim
Date: 2/15/2025
"""

################################################################################
# CLASSES
################################################################################
import util
class FeatureModel:

    def __init__(self, partition, feature):
        """
        The contructor takes a partition (Partition of the training dataset) and
        a feature (string) which is the sole feature that will be used for
        predictions.
        It takes a feature in as well, the one we plan to model and it creates the probability dictionary 
        with values of the feature as keys and the probabilities as values.
        """
        self.feature = feature
        self.prob_dict = {}
        possible_values = partition.F[feature]
        for value in possible_values:
            total = 0
            pos = 0
            for example in partition.data:
                if example.features[feature] == value:
                    total+=1
                    if example.label == 1:
                        pos+=1
            self.prob_dict[value] = pos/total if total!=0 else 0.0

        

    def classify(self, example, threshold):
        """
        This helper method classifies one example (Example from the test
        dataset) as -1 or 1 using the given threshold.
        """
        value = example.features[self.feature]
        prob = self.prob_dict[value]
        return 1 if prob >= threshold else -1

    def confusion_matrix(self,partition,threshold):
        """
        uses model to return the confusion matrix for the given partition, 
        it returns True Positive, True Negative, False Positive, Fase negative.
        """
        data = partition.data
        TP,TN,FP,FN = 0,0,0,0
        for example in data:
            pred = self.classify(example,threshold)
            if pred == +1:
                if example.label == 1:
                    TP+=1
                else:
                    FP+=1
            else:
                if example.label == 1:
                    FN+=1
                else:
                    TN+=1
        return TP,TN,FP,FN

################################################################################
# MAIN
################################################################################

def main():
    # TODO: test your class here
    args = util.parse_args()
    train_filename = args.train_filename
    test_filename = args.test_filename
    #the training data
    train_data = util.read_arff(train_filename)
    test_data =  util.read_arff(test_filename)

    model = FeatureModel(train_data, "cap-shape")
    print(model.feature,model.prob_dict)
    threshold = 0.5
    #confusion matrices
    TP,TN,FP,FN = model.confusion_matrix(train_data,threshold)
    print(f"TN: {TN},\tFP: {FP}")
    print(f"FN: {FN},\tTP: {TP}")
    print()
    print("Test Data Confusion Matrix:")
    TP,TN,FP,FN = model.confusion_matrix(test_data,threshold)
    #recall and precision
    print(f"TN: {TN},\tFP: {FP}")
    print(f"FN: {FN},\tTP: {TP}")
    print(f"Accuracy: {(TP+TN)/(TP+TN+FP+FN)}, ({TP+TN} out of {TP+TN+FP+FN})")
    print(f"False Positive {FP/(FP +TN)}")
    print(f"True Positive: {TP/(TP+FN)}")

if __name__ == "__main__":
    main()
