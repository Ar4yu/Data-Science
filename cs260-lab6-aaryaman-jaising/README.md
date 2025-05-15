[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/e-vSfM0f)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18751757&assignment_repo_type=AssignmentRepo)
## CS260 Lab 6: Information Theory

Name 1: Aaryaman Jaising

Number of Late Days Using for this lab: 0

---

### Analysis

1. For Part 2, was the feature selected by information gain ever different from the feature selected by classification accuracy? Explain your results for each of the 4 datasets.
Ans:    For Part 2, I compared the best features selected by information gain versus classification accuracy on four different datasets.

Movies Dataset:
Running python3 best_feature.py -r data/movies_train.arff yielded:

"Information Gain:"
Type: 0.306099
Length: 0.306099
Director: 0.557728
Famous_actors: 0.072780
→ Best feature by information gain: Director
Classification Accuracy:
Type: 0.777778
Length: 0.777778
Director: 0.888889
Famous_actors: 0.666667
→ Best feature by accuracy: Director

Interpretation: Both methods agree that Director is the most informative feature for the movies dataset.



"Diabetes Dataset:"
The results showed:

Information Gain: Best feature is plas<=127.5
Classification Accuracy: Best feature is plas<=143.5
Interpretation: The difference here suggests that while splitting at plas<=127.5 minimizes overall uncertainty (entropy), the split at plas<=143.5 results in a higher proportion of correctly classified examples. This discrepancy occurs because information gain focuses on reducing entropy, whereas classification accuracy measures how well the majority vote within each partition predicts the actual labels.


"Heart Dataset:"
For the heart dataset:

Both methods selected thal as the best feature.
Interpretation: The consistency in selecting thal indicates that it robustly reduces uncertainty and yields high prediction accuracy.


"Tennis Dataset:"
Running python3 best_feature.py -r data/tennis_train.arff yielded:

Information Gain:
Outlook: 0.246750
Temperature: 0.029223
Humidity: 0.151836
Wind: 0.048127
→ Best feature by information gain: Outlook
Classification Accuracy:
Outlook: 0.714286
Temperature: 0.642857
Humidity: 0.714286
Wind: 0.642857
→ Best feature by accuracy: Outlook
Interpretation: Here, both methods agree on Outlook as the best feature, demonstrating its strong predictive power in the tennis dataset.



2. For your Shannon code based on the vaccine Twitter data, what is the average number of bits needed to send one character? Is this higher or lower than you expected?

  Number of Unique Characters in Twitter Dataset: 105
  Average Number of bits per character: 5.75206707476283

  Even though there are 105 unique characters—meaning a fixed-length encoding would require 7 bits per character (since 2^6 = 64 is too few to represent all 105 symbols)—Shannon encoding leverages the non-uniform distribution of characters. More frequent characters are assigned shorter codes, while less frequent ones get longer codes. This results in an average of about 5.75 bits per character, which is significantly lower than the 7 bits needed for a fixed-length scheme.



  PS: Secret Revealed:
  "" 
 
    fact
    the australian giant cuttlefish is the world's largest species of cuttlefish.
    
  ""

---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below): 4

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy): 3

3. Describe the biggest challenge you faced on this lab:
    Figuring out the two pointer approach for the decoder because it is not a trivial solution, it was quite interesting. 
    Additionally, using subsets for the conditional entropy also was a tricky approach.
