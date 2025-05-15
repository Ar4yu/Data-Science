[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/c6x4H80D)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18152635&assignment_repo_type=AssignmentRepo)
## CS260 Lab 4: Evaluation Metrics

Name 1: Aaryaman Jaising

Name 2: Aiden Kim 

Number of Late Days Using for this lab: 0

---

### Analysis

1. In this lab we are thinking about poisonous vs. edible mushrooms. For this application, would you prefer a higher or lower classification threshold? Explain your reasoning.

   In this lab, we would prefer a lower classifcation threshold because we are ok with the false positives than the false negatives since we are talking about poisonous mushrooms. Better safe than sorry. 

2. Come up with one example application where you would prefer a low (below 50% threshold) and one where you would prefer a high (above 50% threshold). (Excluding examples from class and from this lab.)

   One example of a low threshold that we would prefer would be disease , not knowing you have the disease would suck. One example of a high threshold that we would prefer is flagging important emails, you don't want too many emails to be flagged positive because it would be annoying.

3. What is the runtime (in big-O notation) of creating a single feature decision tree model (decision stump)? Assume: `n` training examples, each with `p` features, the feature in question has `v` possible values, and the outcome is binary. 

  For one feature, it would be O(nv) according to our implementation. p is irrelevant because we use only one feature. What we did was for each value in v, we looped over the entire data set, of size n, thus leading to n*v steps. Therefore, we have time complexity of O(nv)

1. Briefly describe your AUC algorithm and which were the resulting top five features from this step. Did they match the features from your visual inspection?
  In our AUC algorithm we calculated the incremental distances between points using triangle and rectangle formula. When we did this, we were able to get 3 out of the 5 features. We used the following code:

   for f in train_data.F:
        FPR_list,TPR_list = create_roc(train_data,test_data,f)
        auc = compute_AUC(FPR_list,TPR_list)
        auc_list[f] = auc

    sorted_auc = dict(sorted(auc_list.items(),key= lambda item: item[1],reverse=True))
    print("Sorted area under the curve")
    print(sorted_auc)
    # Top five are: 'odor': 0.9874172185430463, 'spore-print-color': 0.9016440736047688, 'gill-color': 0.8790932491771662, 'ring-type': 0.8109928993234036, 'population': 0.77548075007371
---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)
  3

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  2

3. Describe the biggest challenge you faced on this lab:
The area under the curve, because we did not realize that the threshold goes from the top of the curve to the bottom. We ixed that using absolute values.
