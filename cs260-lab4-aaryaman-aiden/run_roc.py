"""
The run-roc py for Lab 4
We create the ROC curves for each feature in the mushroom dataset.
Author: Aaryman Jaising and Aiden Kim
"""

# python imports
import util
import numpy as np
import matplotlib.pyplot as plt
import FeatureModel
import random
################################################################################
# MAIN
################################################################################

def main():

    # TODO: parse args and then call util.read_arff to read both train/test data
    args = util.parse_args()
    train_filename = args.train_filename
    test_filename = args.test_filename

    train_data = util.read_arff(train_filename)
    test_data =  util.read_arff(test_filename)

    print(f"training data: {train_data.n}")
    print(f"test data: {test_data.n}")

    print("Train data Features", train_data.F)
    # print("Train Data data", train_data.data)
    # TODO: for each feature, call create_roc
    #top 5 features'
    top_five = ['odor','gill-color','bruises','ring-type','stalk-surface-above-ring']
    for f in top_five:
        FPR_list,TPR_list = create_roc(train_data,test_data,f)
        #to randomize the colors
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        #plot the points 
        plt.plot(FPR_list,TPR_list,marker='o',linestyle = "-",label= f"Feature: {f}",color = color)
        plt.xlabel("FPR")
        plt.ylabel("TPR")
        plt.title("ROC Curve")
        plt.legend()
    # plt.show()
    #plt.savefig("figures/roc_curve_top5.pdf")


    auc_list = {}
    for f in train_data.F:
        FPR_list,TPR_list = create_roc(train_data,test_data,f)
        auc = compute_AUC(FPR_list,TPR_list)
        auc_list[f] = auc

    sorted_auc = dict(sorted(auc_list.items(),key= lambda item: item[1],reverse=True))
    print("Sorted area under the curve")
    print(sorted_auc)
    # Top five are: 'odor': 0.9874172185430463, 'spore-print-color': 0.9016440736047688, 'gill-color': 0.8790932491771662, 'ring-type': 0.8109928993234036, 'population': 0.77548075007371

    
################################################################################
# HELPER FUNCTIONS
################################################################################

def create_roc(train_partition, test_partition, feature):
    """
    Computes ROC curves and returns list of TPR and FPR
    Takes in train and test partition data and feauture we want to model.
    """
    # TODO: create a model based on the training data and the given feature
    model = FeatureModel.FeatureModel(train_partition,feature)
    thresholds = np.linspace(-0.0001,1.1,20)
    TPR_list = []
    FPR_list = []
    #for the thresholds to find the roc curve
    for threshold in thresholds:
        TP,TN,FP,FN = model.confusion_matrix(test_partition,threshold)
        TPR = TP/(TP+FN)
        FPR = FP/(FP+TN)
        TPR_list.append(TPR)
        FPR_list.append(FPR)
    return FPR_list,TPR_list
    # plt.plot(FPR_list,TPR_list,marker='o',linestyle = "-",label= f"Feature: {feature}")
    # plt.xlabel("FPR")
    # plt.ylabel("TPR")
    # plt.title("ROC Curve")
    # plt.legend()
    # plt.show()
    # TODO: for a variety of thresholds, classify all test examples and create
    # a ROC curve based on the resulting confusion matrices

    # TODO: plot the ROC curve using plt.plot


# computing the area under the curve
def compute_AUC(x,y):
    """
    We compute the AUC using triangle and rectangle area between consecutive points, 
    x,y coordinates of the points on the curve.
    """
    total_area = 0
    for i in range(1,len(y)):
        temp_area = 0
        temp_area += min(y[i],y[i-1])*abs(x[i]-x[i-1])
        temp_area += (1/2) * abs(y[i]-y[i-1]) * abs(x[i]-x[i-1])
        total_area += temp_area
    return total_area
if __name__ == "__main__":
    main()
