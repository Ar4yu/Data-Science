[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cBB4ygkW)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17799747&assignment_repo_type=AssignmentRepo)
## CS260 Lab 1: Computing and Plotting in Python

Name: Aaryaman Jaising

Number of Late Days Using for this lab: 0

---

### Analysis

Part 1
Finally, what is the big-O runtime of each of your binary search algorithms? Explain your answers :
Both algorithms have Big-O of Log(n) to the base 2. This is because we keep eliminating half of the sorted list that doesn't contain our query. The max time to reach the entire list ( if query is not in the list) is reached in log(n) to the base 2 steps for a list of size n.

Part 2
Array Splicing: 
- 1 ex_array_2d[2] = [23 68 78 40] since it would be the row with index 2, using Rom-com = rows and columns
- 2 ex_array_2d[:,1] = [68,58,68,34,73] column with index 1
- 3 ex_array_2d[:3,:2] = [[30,68],[82,58],[23,68]]
- 4 ex_array_2d[2:4,:] = [[23 68 78 40],[18 34 25 76]] index rows 2 and 3

Array Concat:
The code throws an error because the numpy arrays do not have matching dimensions on the required axis. i.e. since we're concatinating on axis 1, axis 0 needs to match but their shapes are 5 and 1 respectively (5*4) and (1*4), however the concatenation does work on axis 0 because both have shape 4 on axis 1, i.e. axis 1 matches. 

Part 3
Matplotlib:
The quadratic function opens downwards, i.e. it is a concave function. The cubic function seems to be convex and increases exponentially. Also, with more points the curves are much smoother.

Part 4

In the object oriented Student class problem:
In dictionaries when you try to add with the same key, it simply replaces the old key's value with the new value. So the keys act like a set, no duplicate keys, also when you add a different key with a repeated value, it allows you to do that, because values can be repeated.

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)
  5

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  2
3. Describe the biggest challenge you faced on this lab:
  It was proabably commenting and shifting to python syntax from java. Also using new functions took some time to understand.