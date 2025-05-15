[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sMJ7vCUR)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18864655&assignment_repo_type=AssignmentRepo)
## CS 260 Lab 7 - Logistic Regression and Visualization

Name 1: Aaryaman Jaising

Number of Late Days Using for this lab:

---

### Analysis Questions

1. So far, we have run logistic regression and Naive Bayes on different types of datasets. Why is that? Discuss the types of features and labels that we worked with in each case.

        Question 1: Comparison of Logistic Regression and Naive Bayes
        The key difference between when we use Logistic Regression versus Naive Bayes comes down to the nature of the features and labels:

        Logistic Regression works best with continuous features and binary labels. It models the probability of the binary outcome directly using a logistic function of a linear combination of the features. The phoneme and Challenger datasets in this lab had continuous input features (like temperature measure) with binary class labels.

        Naive Bayes is particularly suited for discrete/categorical features . It works by applying Bayes' theorem with the "naive" assumption of conditional independence between features. In previous labs, we used it for the tennis dataset, housing dataset,zoo dataset. All of these had primarily categorical features.

        The fundamental distinction is that Logistic Regression learns the decision boundary directly, while Naive Bayes is a generative model that learns the joint probability distribution P(X,y). Logistic Regression tends to perform better with continuous features and sufficient training data, while Naive Bayes can work well with limited data and discrete features.

2. Regarding the Challenger data specifically, what was your final probability of an accident after fitting the model? Is this what you expected? Based on this value, would you have recommended the Challenger be launched on 1/28/86? What data and/or modeling might have helped increase the confidence of our prediction?


        Question 2: Challenger Data Analysis

        For the Challenger dataset, my final probability of an accident at the launch temperature (31°F) was approximately 1. This high probability makes sense given:

        The training data shows a clear trend of more O-ring failures at lower temperatures

        31°F was much colder than any previous launch in the dataset

        Based on this model, I would not have recommended launching on 1/28/86. The predicted failure probability was extremely high (approx 1), suggesting near certainty of an O-ring failure at that temperature.

        To increase confidence in this prediction, we could have benefited from:

         - More historical test data points at very cold temperatures to better estimate the failure curve, /Simulations

         - Additional features beyond just temperature, not sure hwat could have been relevant 

         - Historical data from similar rocket designs

        The visualization clearly shows how the logistic curve fits the training data and predicts near-certain failure at the test temperature. This provides strong visual evidence supporting the model's concerning prediction.
        "
        Accuracy: 1.000000
        1 out of 1 correct
        Confusion Matrix:
        prediction
            0   1
            ------
        0 | 0   0
        1 | 0   1
        Probability Challenger Exploded was:  [1.]
        alpha was 0.005, increased max iterations
        "


Note: Found a slightly more accurate model of the logistic regression for phenome data
"
Accuracy: 0.887500
71 out of 80 correct
Confusion Matrix:
   prediction
      0   1
    ------
0 | 37   3
1 | 6   34
"
---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide your answer as a single integer on the line below)
4

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1 being very easy)
4

3. Describe the biggest challenge you faced on this lab:
    Finding the right alpha values and messing with the hyper parameters was tricker than expected. I ended up increasing max iterations and reducing learning rate.