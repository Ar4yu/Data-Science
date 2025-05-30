# CS260 Final Project: Interpretable Medical Diagnosis Using Decision Trees and Naive Bayes
## Authors: Aaryaman Jaising and Rustom Dubash
### Course: CS260 – Data Science
### Date: May 15, 2025
# Project Title: Decision Tree vs. Naive Bayes for Interpretability in Medical Diagnosis

# Notes on the Code
To reproduce our exact results from the presentation:
1. Results Full Tree (Figure 1)
- Set max depth to 15, (line 76, decision_tree.py)
- Go to output/decision_tree.png
2. Threshold 0.5, all features, Figure (2A), on the left hand side of slide 7.
- Maintain max_depth=2, class_weight={0: 1.0, 1: 2}  (lines 76, 78 decision_tree.py)
- Go to output/decision_tree.png
3. Threshold 0.5, easy features, Figure (2B), on the right hand side of slide 7.
- Maintain max_depth=2, class_weight={0: 1.0, 1: 2}  (lines 106, 108 decision_tree.py)
- Go to output/decision_tree_easy_features.png
4. \* Threshold 0.5, all features, Figure (3A), on the left hand side of slide 8. 
- Maintain threshold = 0.5 (line 60, visualize.py)
- Go to output/DecisionTree_confusion.png
5. \* Threshold 0.5, easy features, Figure (3B), on the right hand side of slide 8. 
- Maintain threshold = 0.5 (line 60, visualize.py)
- Go to output/DecisionTreeEasyFeatures_confusion.png
6. Threshold 0.4, all features, Figure (4A), on the left hand side of slide 9.
- Maintain threshold = 0.4, (line 60, visualize.py)
- Go to output/DecisionTree_confusion.png
7. Threshold 0.4, easy features, Figure (4B), on the right hand side of slide 9.
- Maintain threshold = 0.4, (line 60, visualize.py)
- Go to output/DecisionTreeEasyFeatures_confusion.png
8. Threshold 0.4, all features, Figure (5A), on the left hand side of slide 10.
- Maintain threshold = 0.4, (line 60, visualize.py)
- Go to output/NaiveBayes_confusion.png
9. Threshold 0.4, easy features, Figure (5B), on the right hand side of slide 10.
- Maintain threshold = 0.4, (line 60, visualize.py)
- Go to output/NaiveBayesEasyFeatures_confusion.png

Note: The points marked with a star will need to be changed, the rest are submitted already in that format. 
        
# Scientific Question
This project investigates whether a Decision Tree classifier can be as informative and accurate for predicting diabetes as a Naive Bayes classifier. The motivation stems from the medical need for both accuracy and interpretability in diagnostic models. While Naive Bayes often performs well in terms of accuracy and speed, it lacks interpretability due to its probabilistic nature and assumption of feature independence. In contrast, Decision Trees can provide clear, step-by-step reasoning for their predictions, making them more accessible to patients and medical professionals. This trade-off between transparency and performance framed our core research question: Which algorithm is best suited for real-world, interpretable medical diagnostics?

# Dataset and Preprocessing
We used the Pima Indians Diabetes dataset provided by the National Institute of Diabetes and Digestive and Kidney Diseases. The dataset includes medical data for female patients over the age of 21 and of Pima Indian heritage. The target variable is a binary outcome indicating whether the individual has diabetes. Features include pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, BMI, diabetes pedigree function, and age.

The dataset was heavily imbalanced, with approximately 67% of entries labeled as not diabetic. To address this, we applied class weights in the Decision Tree model and closely monitored recall and false negative rates during evaluation. Preprocessing steps included removing rows with biologically implausible zero values in key features such as glucose, blood pressure, skin thickness, and BMI. The Insulin column was dropped entirely due to the excessive number of missing values. We also created two feature sets for comparison: a full set containing all cleaned variables and a reduced “easy” feature set that excluded glucose, skin thickness, and diabetes pedigree function. The latter was designed to simulate a scenario where only easily obtainable features are available in low-resource clinical environments.

# Methodology
We trained and evaluated two models: a Decision Tree classifier with a maximum depth of 2 and a Gaussian Naive Bayes classifier. Both were trained on the full and reduced feature sets. The Decision Tree included class weights to penalize misclassification of diabetic individuals more heavily, reflecting the higher cost of false negatives in a medical setting.

Each model was evaluated using accuracy, precision, recall, and false negative rate, along with visual tools such as confusion matrices and ROC curves. An important part of our methodology was manual threshold tuning. The default threshold of 0.5 for classification is not always ideal in high-risk domains like healthcare. Therefore, for certain models, we experimented with lowering the threshold to improve recall and reduce false negatives, accepting a potential trade-off with precision.

# Results and Analysis
The Decision Tree trained on the full feature set achieved an accuracy of 73%, with a precision of 0.53 and an excellent recall of 0.97. This indicates that while the model was highly sensitive in detecting diabetic cases, it also produced a significant number of false positives. This over-prediction may be acceptable in a medical setting where it is far more dangerous to miss a diabetic patient than to incorrectly classify a non-diabetic one.

The Decision Tree trained on the reduced "easy" feature set showed lower performance at the default threshold of 0.5, with a false negative rate of 33%. To address this, we manually lowered the classification threshold to 0.4. This change significantly reduced the false negative rate to 6.1%, illustrating how threshold tuning can align model behavior with the specific priorities of a diagnostic context. By lowering the threshold, the model became more aggressive in labeling positive cases, reducing the risk of missing a true diabetic patient at the cost of increasing false positives.

The Naive Bayes classifier on the full feature set achieved a higher overall accuracy of 80%, with a precision of 0.66 and a recall of 0.76. Although this model was generally more accurate, it did not achieve the same level of recall as the Decision Tree. This is a critical distinction, as false negatives—undiagnosed diabetic patients—represent a serious failure in a clinical setting. Naive Bayes on the reduced feature set also performed reasonably well but suffered from similar limitations in recall.

Overall, the Decision Tree models—particularly when adjusted for threshold—offered strong interpretability and high recall, making them well-suited for situations where transparency and early detection are critical. Naive Bayes offered speed and solid baseline performance, but its assumptions about feature independence and probabilistic nature make it less intuitive to interpret without statistical training.

# Conclusion
Our results suggest that Decision Trees provide a valuable balance between interpretability and predictive power in the context of diabetes diagnosis, especially when tuned for higher sensitivity. While Naive Bayes performed better in terms of overall accuracy, it was less effective at identifying diabetic cases under default conditions. Decision Trees offer the additional advantage of being visualized and understood easily by non-technical users, making them more suitable for patient-facing applications.

In summary, if the goal is a high-recall, interpretable model for clinical decision support, Decision Trees—especially with tuned thresholds—may be the more appropriate choice. However, if the goal is to maximize accuracy in a backend system with minimal interpretability requirements, Naive Bayes remains a strong baseline.

# Future Work
If given more time and resources, we would expand the project in several ways. First, we would explore ensemble methods such as Random Forests or Gradient Boosting, which could improve predictive performance while maintaining some degree of interpretability. We would also implement more advanced techniques for handling class imbalance, such as SMOTE or ADASYN. Additionally, we would develop a lightweight diagnostic application using the reduced-feature Decision Tree model for deployment in low-resource settings. Lastly, further investigation into threshold optimization strategies, including ROC-based threshold selection, could help refine decision boundaries more systematically.


# Reflection on AI Tool Use
We used GitHub Copilot and ChatGPT to streamline coding tasks such as argument parsing, data preprocessing, and evaluation scripting. These tools accelerated development by reducing time spent on boilerplate code and debugging. While the core logic and analytical design were our own, AI-assisted tools helped us focus more on the modeling and evaluation aspects of the project. All in all AI use was to simplify using the sckit-learn library usage since it was convenient in understanding hyperparameters and argument formatting and options.
