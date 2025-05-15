[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Dvl1SY4z)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19004282&assignment_repo_type=AssignmentRepo)
## CS260 Lab 8: Statistics

Name 1: Aaryaman Jaising

Number of Late Days Using for this lab: 0

---

### Analysis

1. For the iris flower dataset in Part 1, what genealogical relationships can we infer from the PCA plot? For your other chosen dataset, what conclusions can you draw from the PCA plot? Does the number of visual clusters match the number of labels?
    For Part 1 we notice from the graph that the points are linearly seperated according to principal component one on the x axis. The two principle components effectively reduce the dimensions such that we have vaptured the variation that explains the labels.
    There are 3 visual clusters, that match the three labels for the data: ["Iris Setosa","Iris Versicolour","Iris Virginica"]

    For the other_pca I choose the wine dataset inbuilt in the library. There definitely was some clustering along PC1 when I plotted the graph. However, the first two labels were not as seperable as label 2 and 3.. We may need more components to seperate all of them accurately.

2. For Part 2, include both your p-values below. What is the probabilistic *interpretation* of the p-value in this coin toss situation? Given this interpretation, do you reject the null hypothesis (fair coin) or fail to reject?
      The p-values I got were:
          CLT p-value: 0.00175
          Random trials p-value: 0.00184
      Null Hypothesis: The coin is fair
      Alternative Hypothesis: The coin is not fair        
      The probabilistic interpretation of the p-value is that assuming the null hypothesis is true, the probability of getting a sample of coin tosses as or more extreme than 54 heads out of 80, is 0.00175. (0.175%). Since alpha (significance level) is 0.05, and p-value is less than alpha, we can reject the null hypothesis.

3. For Part 3, include both your p-values below. Do you reject the null hypothesis (genomes from Population 1 and Population 2 are roughly the same size) or fail to reject?
      The p-values are:
        CLT p-value: 0.00190
        Permutation testing p-value: 0.00189

      Null Hypothesis: the populations 1 and 2 are roughly the same size.
      Alternative Hypothesis: The populations 1 and 2 are not the same size.

      The probabilistic interpretation of the p-value is that assuming the null hypothesis is true, the probability of getting a sample of populations with a differnce as or more extreme than the given sample, is 0.00190. (0.19%). Since alpha (significance level) is 0.05, and p-value is less than alpha, we can reject the null hypothesis.



4. (Optional) If you did Part 4, write up your procedure and results here (what were you trying to test, how you went about it, what you found, etc).


---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)
  4

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  2

3. Describe the biggest challenge you faced on this lab:
 Graphing the lines, vertical lines on coin toss