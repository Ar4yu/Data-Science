[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TYBHWPoY)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18029722&assignment_repo_type=AssignmentRepo)
## CS260 Lab 3: Gradient Descent

Name: Aaryaman Jaising

Number of Late Days Using for this lab: 0

---

### Analysis

Part 2: Comment on how close your results are (for `w`) to the provided models from Lab 2.

Ans: The results are very close, almost the same. w is [ 1.90503821e+02 -9.22444604e-02], as compared to lab 2 (190.5,-0.0922)

Part 4:

- a) Include the optimal weights from both your analytic solution and your SGD solution. Comment on any differences between the two models.
  - Analytic Solution: [8.03820875e-17 6.51280605e-01 4.65062749e-01 3.43692235e-01 5.77068966e-03 4.27271975e-01]
  - SGD Solution: [[-3.84127173e-05] [ 6.51201091e-01] [ 4.65091506e-01] [ 3.43761591e-01] [ 5.88586476e-03] [ 4.27319375e-01]]
  - The weights from both methods are nearly identical. The slight differences (on the order of 1e-05) are negligible, and the final cost values differ by less than 0.1. This confirms that our SGD implementation converges to essentially the same optimum as the closed-form analytic solution.


- b) For each model, what was the most important feature? Which features were essentially not important? Do these results make sense to you? Does it matter that we normalized the features first?

For the USA Housing dataset, the features (in order) are:
1. **Avg. Area Income**
2. **Avg. Area House Age**
3. **Area Population**
4. **Avg. Area Number of Rooms** 
5. **Avg. Area Number of Bedrooms**

- **Most Important Feature:**  
The coefficient for **Avg. Area Income** is approximately 0.65, which is the highest among the features. This suggests that the average income is the most significant predictor of housing price.

- **Least Important Feature:**  
The coefficient for **Avg. Area Number of Bedrooms** is extremely small (≈ 0.0058), indicating that this feature contributes very little to predicting the price. This might be due to a high correlation with other features or limited variability in the data.

- **Normalization:**  
Normalizing the features was essential for gradient descent. It ensures that all features are on a similar scale, preventing any single feature (with a large numeric range) from dominating the learning process. Moreover, normalization makes the coefficients directly comparable, aiding in the interpretation of feature importance. It also does not affect the overall model and analysis, simply makes it convenient and easy to interpret. Because we only look at the variation in feature after normalization, that are all scaled to be neutral.




---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)
  4

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  3
3. Describe the biggest challenge you faced on this lab:
The stochastic gradient descent part where i had some trouble reshaping the numpy arrays.
Mismatching of the array shape always creates an issue.