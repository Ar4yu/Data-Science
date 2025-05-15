[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/W5vIS8oT)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18337438&assignment_repo_type=AssignmentRepo)
## CS260 Lab 5: Naive Bayes

Name 1: Aaryaman Jaising

Number of Late Days Using for this lab: 0

---

### Analysis

#### Part 2

1. In this lab we will be considering sex as a protected attribute, and seeing if we can predict sex from the remaining attributes. First, compute the fractions of males and females in the *training* data.

  Ans:  - num train = 28998 , num classes = 2
        - num test  = 7419 , num classes = 2
        - Training Data - Number of Males: 19633, females: 9365, Total = 28998
        - Percentage Males = 67.70%, Females Percentage = 32.30%

2. Given these ratios, if an algorithm to predict sex randomly flipped a coin for every *test* example, what confusion matrix would result? What overall classification accuracy would result?

    Ans:  - Using Random Coint to Predict
          True Negative: 2415     False Positive: 2478
          False Negative: 1211    True Positive: 1315
          - Accuracy: 0.5027631756301388
          Note: This changes because we are using random.random.

3. What if an algorithm always predicted the majority class? What would the confusion matrix look like in this scenario? What overall classification accuracy would result?

    Ans:  - Using Majority to Predict, i.e. all males predicted
          True Negative: 4893     False Positive: 0
          False Negative: 2526    True Positive: 0
          - Accuracy: 0.6595228467448443
#### Part 4

1. Just temporarily, remove the LaPlace counts from your code and run your method again. What error do you obtain? What does this error actually mean about the data?

  Ans: The error I got is: 
          " Traceback (most recent call last):
          File "/Users/aaryamanjaising/Library/CloudStorage/OneDrive-Personal/Haverford/Sem 6/Data_Science/cs260-lab5-aaryaman/run_NB.py", line 211, in <module>
            main()
            ~~~~^^
          File "/Users/aaryamanjaising/Library/CloudStorage/OneDrive-Personal/Haverford/Sem 6/Data_Science/cs260-lab5-aaryaman/run_NB.py", line 119, in main
            nb = NaiveBayes.NaiveBayes(train_partition)
          File "/Users/aaryamanjaising/Library/CloudStorage/OneDrive-Personal/Haverford/Sem 6/Data_Science/cs260-lab5-aaryaman/NaiveBayes.py", line 47, in __init__
            self.prob_dict[l][feature][val] = math.log((tmp)/(self.label_counts[l] + num_values)) #includes laplace counts
                                              ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ValueError: math domain error "

        This means that certain counts of values for certain labels are 0  and thus their probabilities are 0. This breaks the function when taking a log because log of 0 does not exist.



2. When trying to predict sex from the other attributes, what accuracy do you obtain? Is this higher or lower than you would expect with one of the naive strategies from Part 2?
                num train = 28998 , num classes = 2
                num test  = 7419 , num classes = 2

                ===== Naive Bayes Classification Results =====
                Overall Accuracy: 0.8188 (6075 out of 7419 correct)

                Confusion Matrix:
                Actual\Pred            0           1
                ------------------------------------
                0                   3734        1159
                1                    185        2341
          This strategy is more accurate than both naive strategies in Part 2. If we compare it to part two with the baseline split we will see that it is higher than (Percentage Males = 67.70%, Females Percentage = 32.30%), this tells us that the data are somewhat correlated to the sex variable.

Legend:
Rows represent the actual labels, and columns represent the predicted labels.

3. Re-run your method with the `corrected` train/test data. What accuracy do you obtain now? Explain the difference between the two datasets and why this accuracy change makes sense.

  Ans:    (venv) aaryamanjaising@mac cs260-lab5-aaryaman % python3 run_NB.py -r data/1994_census_cleaned_corrected_train.csv -e data/1994_census_cleaned_corrected_test.csv 
          num train = 28998 , num classes = 2
          num test  = 7419 , num classes = 2

          ===== Naive Bayes Classification Results =====
          Overall Accuracy: 0.7771 (5765 out of 7419 correct)

          Confusion Matrix:
          Actual\Pred            0           1
          ------------------------------------
          0                   3735        1158
          1                    496        2030

          Legend:
          Rows represent the actual labels, and columns represent the predicted labels.

         

When running the Naive Bayes classifier on the corrected dataset, the accuracy dropped from 81.88% to 77.71%.

This makes sense because the corrected dataset likely removes data inconsistencies, redundancies, or biases that made classification easier in the uncorrected version. The lower accuracy suggests the model now has less redundant information to rely on, making the task more challenging but also more realistic.
An example I found was that in the "relationship variable" instead of husband and wife, a gender neutral term of partner or spouse was used. Since having 'husband' or 'wife' as values show a high correlation with pur pretected variables of male and female it would be better to edit them in the corrected version
Leading to a lower model accuracy.




4. What (if anything) is concerning about being able to predict such a protected attribute
from the other attributes (especially using an algorithm like Naive Bayes that does not explicitly account for feature interactions)?  If the actual "label" were "hired" or "not hired" for a job, and you
were responsible for making this decision, how would you deal with data where features were
redundantly encoded?

Ans: Predicting a protected attribute like sex using other features is concerning because it exposes hidden biases in the data. Even though Naive Bayes doesn’t explicitly model feature interactions, correlations in the dataset (e.g., job type, income) can still reveal the features like sex that they are correlated with.

In a hiring scenario, if a model learns to predict outcomes based on gender-related patterns, it could lead to discrimination—even if sex isn't directly included as a feature. To prevent this, we should:

Remove or decorrelate features that strongly predict protected attributes. Like 'husband /wife' in the corrected data.
Use fairness-aware models that minimize biased decision-making.
Regularly evaluate model outputs to ensure no unfair patterns emerge. Like having a human in the process to identify discrepancies the machine cannot.

The key takeaway: Just because a model can predict something doesn’t mean it should. Like we can get a better fitting model, but if it learns something in a way we don't want it to function because of correlation it is really harmful. Like for example of model that evaluated court cases and then performed predictions that were racially discriminitive.

---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)
  5

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  3

3. Describe the biggest challenge you faced on this lab:
  making the naive bayes model took a lot of effort and thought. Also the confusion matrices were hard to construct.