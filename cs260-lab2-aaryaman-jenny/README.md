[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/R-b_MeyN)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17951540&assignment_repo_type=AssignmentRepo)
## CS260 Lab 2: Modeling Climate Change

Name 1: Aaryaman Jaising

Name 2: Jenny Le

Number of Late Days Using for this lab:
0
---

### Analysis

Part 2: Describe the patterns you see in the residuals. Based on these patterns, which model do you think is a better fit for this data?

Ans: For The linear equations residuals, the residuals seem to have a quadratic pattern. However, for the quadratic regression they seem to be random, and that is a good sign. This indicates that the linear regression is not able to capture all the variation in the data and the quadratic model does it better.

Part 3: Describe what you observe. Based on these visualizations, which model do you think is a better fit? How would you advise governments who are trying to make policy decisions based on this type of model fitting process?

Ans: The linear model is a better predictor for future data than the quadratic model. The quadratic model seems to fit the training data better, i.e. the time from 1979-2012, but it seems tooo specific to the data. Therefore, it fails to remain accurate for future data. The linear function in comparison: does not fit the training data as well, however it captures the general trend better, predicting the future sea ice extent better.
I would advise the government to use a simpler model that captiures the overall trend instead of a more complex model that leads to the risk of overfitting.

Part 4: Describe the pattern you observe (in the polynomial models). Based on these preliminary visualizations, which model would you choose and why?
Looking at the elbow plot, which degree would you choose? Explain your answer.

Ans: Based on these polynomial models, as the degree n of a polynomial model increases, the model appears to fit better to the data. I would choose the 4 degrees plot as it captures the general trend of the data while not being skewed to any outliers. The elbow plot shows the RSS beginning to plateau at around degree 3. Looking at this plot, I would choose a degree 4 plot as the best fitting model, as it is the polynomial model of the smallest degree that captures the smallest RSS value after the elbow point. Therefore, this model's error is relatively low and captures the general trend of the data pretty well. 


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
  The biggest challengse were figuring out how to compute the predicted value for any n-degree model and how to choose the best fitting model by analyzing the graphs visually.
---

### Coefficients for Part 4

~~~
deg_0_coef = [1.13010595]

deg_1_coef = [2.4464070947147207, -2.816353589568698]

deg_2_coef = [2.522610178119313, -3.27003073191282, 0.4743087284609393]

deg_3_coef = [1.2231425230496584, 10.649616212253513, -34.083679747347574, 23.590230897814727]

deg_4_coef = [0.8075214798200756, 17.32934850900337, -62.32907523274797, 66.75220156315058, -21.61184507602993]

deg_5_coef = [1.1537400009153576, 9.784042834672174, -14.963934203443742, -54.05134690879839, 111.9406595086277, -53.20467363235635]

deg_6_coef = [1.6031281515537332, -2.212955964351817, 87.09165569133722, -440.6384252637192, 832.5418657076268, -698.5859135919, 221.439066525518]

deg_7_coef = [1.0048620515132924, 17.4112052205856, -133.45588391947206, 713.2351017847259, -2320.831952624806, 3938.208550304347, -3249.3507974432723, 1036.2869129041017]

deg_8_coef = [0.8889729225247591, 21.927863684690806, -196.3956341264095, 1135.1023058754872, -3863.15628401735, 7177.078002707203, -7143.712758937181, 3524.932857125692, -654.5246542101304]

deg_9_coef = [6.455577860121968, -214.55025432038786, 3518.6484115354933, -28016.264919570815, 126197.74461140906, -343436.25785927917, 574211.0815161027, -575789.2765246094, 317309.99905972165, -73803.67907566673]

deg_10_coef = [5.571266255808752, -173.07147738443035, 2771.613686468927, -21023.423222254118, 87668.04317051847, -210606.67961073387, 280101.8712329003, -158297.13764038868, -49517.323077016044, 107648.64893355407, -38599.19918692205]
~~~
