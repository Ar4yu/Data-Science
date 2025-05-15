"""
Partition and Example objects, along with entropy and best feature functions

Author: Aaryaman Jaising
Date: Tuesday, 18th March

"""

################################################################################
# CLASSES
################################################################################
import math
class Example:

    def __init__(self, features, label):
        """Helper class (like a struct) that stores info about each example."""
        # dictionary. key=feature name: value=feature value for this example
        self.features = features
        self.label = label

class Partition:

    def __init__(self, data, F):
        """Store information about a dataset"""
        # list of Examples
        self.data = data
        self.n = len(self.data)

        # dictionary. key=feature name: value=list of possible values
        self.F = F


    def entropy(self):
        """
        Returns entropy of entire base data only on label
        """
        pos = 0
        neg = 0
        for example in self.data:
            if example.label == 1:
                pos+=1
            else:
                neg+=1
        pos_prob = pos/(pos+neg)
        neg_prob = neg/(neg+pos)
        entropy = 0.0
        if pos_prob > 0:
            entropy -= pos_prob*math.log2(pos_prob)
        if neg_prob > 0:
            entropy -= neg_prob*math.log2(neg_prob)    
        return entropy
    
    def _entropy_of_subset(self, subset):
        """
        Helper function to compute entropy for a subset of examples.
        """
        n_subset = len(subset)
        if n_subset == 0:
            return 0
        pos = 0
        for example in subset:
            if example.label == 1:
                pos+=1
        neg = n_subset - pos
        p_pos = pos / n_subset
        p_neg = neg / n_subset
        entropy = 0.0
        if p_pos > 0:
            entropy -= p_pos * math.log2(p_pos)
        if p_neg > 0:
            entropy -= p_neg * math.log2(p_neg)
        return entropy
    
    def conditional_entropy(self, feature):
        """
        Compute the conditional entropy H(y|X) for a given feature.
        """
        # Partition the examples by the feature's values.
        value_counts = {}
        value_examples = {}
        for ex in self.data:
            val = ex.features[feature]
            if val not in value_counts:
                value_counts[val] = 0
                value_examples[val] = []
            value_counts[val] += 1
            value_examples[val].append(ex)
        
        cond_entropy = 0.0
        for val, count in value_counts.items():
            weight = count / self.n
            subset_entropy = self._entropy_of_subset(value_examples[val])
            cond_entropy += weight * subset_entropy
        return cond_entropy
    
    def information_gain(self, feature):
        """
        Compute the information gain of a given feature.
        IG(feature) = H(y) - H(y|feature)
        """
        overall_entropy = self.entropy()
        cond_entropy = self.conditional_entropy(feature)
        return overall_entropy - cond_entropy

    def best_feature(self):
        """
        Iterate through all features and return the one with the maximum information gain.
        Also prints each feature's information gain.
        """
        best_gain = -1
        best_feature = None
        print("Info Gain:")
        for feature in self.F:
            gain = self.information_gain(feature)
            print(f"{feature}, {gain:.6f}")
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
        return best_feature
    
    def classification_accuracy(self, feature):
        """
        For a given feature, predict the label for each example based on the majority label
        for the feature value, and compute the overall classification accuracy.
        """
        # Compute majority label for each feature value.
        value_majority = {}
        for value in self.F[feature]:
            # Get all examples with the current feature value.
            subset = [ex for ex in self.data if ex.features[feature] == value]
            if not subset:
                continue
            # Count positive and negative labels.
            pos = sum(1 for ex in subset if ex.label == 1)
            neg = len(subset) - pos
            # Majority label: if tie, you can choose one (here, we choose 1).
            majority_label = 1 if pos >= neg else -1
            value_majority[value] = majority_label

        # Use the majority labels to predict for each example and count correct predictions.
        correct = 0
        for ex in self.data:
            predicted = value_majority.get(ex.features[feature])
            if predicted is not None and predicted == ex.label:
                correct += 1

        return correct / self.n if self.n > 0 else 0

    def best_feature_by_accuracy(self):
        """
        Computes the classification accuracy for each feature (using majority vote for each
        feature value) and returns the feature with the highest accuracy.
        """
        best_acc = -1
        best_feature = None
        print("Classification Accuracy:")
        for feature in self.F:
            acc = self.classification_accuracy(feature)
            print(f"{feature:15s}, {acc:.6f}")
            if acc > best_acc:
                best_acc = acc
                best_feature = feature
        return best_feature

