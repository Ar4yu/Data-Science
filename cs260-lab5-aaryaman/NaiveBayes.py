"""
CS260 Lab 5: Implementation of Naive Bayes Model
Author: Aaryaman Jaising
Date: Feb 21, 2025
"""
from run_NB import Partition, Example
from collections import OrderedDict
import math
class NaiveBayes:

    def __init__(self, partition: Partition):
        """
        Sets up all probabilities that will be
        necessary for classifying an example later on, saves it in self.prob_dict

        argument: partition - training data set

        stores: self.log_priors, contains log priors for each class
        self.label_counts: stores same info as log priors, except simply the counts. Needed later for prob_dict 
        """
        #Calculate log prior
        self.label_counts = OrderedDict()
        self.log_prior = OrderedDict()
        for l in range(partition.K):
            self.log_prior[l] = 0
            self.label_counts[l] = 0
        for example in partition.data:
            self.log_prior[example.label] +=1
            self.label_counts[example.label] += 1
        for label in self.log_prior:
            self.log_prior[label] = math.log((self.log_prior[label]+1)/(partition.n+partition.K))
        
        #calculating probability dictionary
        #First we initialize the dictionary
        self.prob_dict = OrderedDict()
        for l in range(partition.K):
            self.prob_dict[l] = OrderedDict()
            for feature in partition.F:
                self.prob_dict[l][feature] = OrderedDict()
                for value in partition.F[feature]:
                    self.prob_dict[l][feature][value] = 0

        for example in partition.data:
            for f in example.features:
                self.prob_dict[example.label][f][example.features[f]] +=1
        
        for l in self.prob_dict:
            for feature in self.prob_dict[l]:
                num_values = len(partition.F[feature])
                for val in self.prob_dict[l][feature]:
                    tmp = self.prob_dict[l][feature][val]
                    self.prob_dict[l][feature][val] = math.log((tmp+1)/(self.label_counts[l] + num_values)) #includes laplace counts

       
        

    def classify(self, x_test):
        """
        based on the dictionary of features x_test, returns the most
        likely class (integer)
        calculates the bayes probability for each class given the data and conditions on the same.
        returns class k of y with max probability
        """
        best_label = None
        best_log_prob = -math.inf

        for l in self.log_prior:
            curr_prob = self.log_prior[l]
            for feature,value in x_test.items():
                curr_prob += self.prob_dict[l][feature][value]
            if curr_prob > best_log_prob:
                best_label = l
                best_log_prob = curr_prob
        return best_label    


    def predict(self, test_partition):
        """
        Classifies all examples in test_partition and computes accuracy.
        Returns:
            - predictions: list of predicted labels
            - accuracy: float (correct predictions / total)
            - confusion_matrix: dict of dicts for actual vs. predicted counts
        """
        predictions = []
        correct = 0
        confusion_matrix = {label: {pred: 0 for pred in self.label_counts} for label in self.label_counts}

        for example in test_partition.data:
            predicted_label = self.classify(example.features)
            predictions.append(predicted_label)

            # Update accuracy count
            if predicted_label == example.label:
                correct += 1
            
            # Update confusion matrix
            confusion_matrix[example.label][predicted_label] += 1

        accuracy = correct / test_partition.n
        return predictions, accuracy, confusion_matrix


    def print_results(self, accuracy, confusion_matrix):
        """
        Prints the Naive Bayes classification results in a formatted table,
        including overall accuracy, total predictions, and the number of correct predictions.
        
        Args:
        accuracy (float): The overall accuracy of the model (fraction correct).
        confusion_matrix (dict): Nested dictionary representing actual vs. predicted counts.
        """
        # Compute total predictions and the number of correct predictions (diagonal sum)
        total = sum(sum(row.values()) for row in confusion_matrix.values())
        correct_count = sum(confusion_matrix[label][label] for label in confusion_matrix)
        
        # Header for the results
        print("\n===== Naive Bayes Classification Results =====")
        print(f"Overall Accuracy: {accuracy:.4f} ({correct_count} out of {total} correct)\n")
        print("Confusion Matrix:")
        
        # Determine sorted list of labels for consistent ordering
        labels = sorted(confusion_matrix.keys())
        
        # Calculate column width based on the longest label or header string
        header_label = "Actual\\Pred"
        col_width = max(max(len(str(label)) for label in labels), len(header_label)) + 1
        
        # Create header row for predicted labels
        header_row = header_label.ljust(col_width)
        for label in labels:
            header_row += str(label).rjust(col_width)
        print(header_row)
        
        # Print a separator line
        print("-" * len(header_row))
        
        # Print each row: actual label followed by counts for each predicted label
        for actual in labels:
            row = str(actual).ljust(col_width)
            for pred in labels:
                row += str(confusion_matrix[actual][pred]).rjust(col_width)
            print(row)
        
        # Print legend for clarity
        print("\nLegend:")
        print("Rows represent the actual labels, and columns represent the predicted labels.\n")
