"""
CS260 Lab 2: Regression analysis of sea ice extent using pandas, numpy and matplotlib
Author: Aaryaman and Jenny
Date: 1/30/25
"""

# python libraries
import optparse
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

################################################################################
# MAIN
################################################################################

def main():
    # reading in data
    #part 1
    data = pd.read_csv("data/sea_ice_1979-2012.csv",header=None)
    print(data.head())
    plt.scatter(data[0],data[1])
    #labels and titles
    plt.xlabel("Year")
    plt.ylabel("Sea Ice Extent (Millions of Square Kilometers)")
    plt.ylim((0,10))
    #plt.xlim((1970,2020))
    plt.title("Sea Ice Extent from 1979-2012")
    plt.savefig("figures/part1.pdf", format='pdf')
    plt.show()
    plt.clf()

    #Part 2
    #Redo plotdata = pd.read_csv("data/sea_ice_1979-2012.csv",header=None)
    print(data.head())
    plt.scatter(data[0],data[1])
    #labels and titles
    plt.xlabel("Year")
    plt.ylabel("Sea Ice Extent (Millions of Square Kilometers)")
    plt.ylim((0,10))
    #plt.xlim((1970,2020))
    plt.title("Sea Ice Extent from 1979-2012")

    #Start with coefficients
    deg_1_coef = [190.5038227644984, -0.09224446142042844]

    deg_2_coef = [-15150.155305067638, 15.283380627913214, -0.0038525745647042583]
    x1 = np.linspace(1979,2012,500)
    y1 = deg_1_coef[0] + deg_1_coef[1]*x1 
    y2 = deg_2_coef[0] + deg_2_coef[1]*x1 + deg_2_coef[2]*(x1**2)

    plt.plot(x1,y1,label = "Linear")
    plt.plot(x1,y2,label = "Quadratic")
    plt.legend()
    plt.savefig("figures/part2_deg1&2.pdf",format = 'pdf')
    plt.show()
    plt.clf()
    #Part 2 resiuals
    y1_predict = predict(data[0],deg_1_coef)
    y2_predict = predict(data[0],deg_2_coef) 
    resid_1 = []
    resid_2 = []
    for i in range(len(data[1])):
        resid_1.append(data[1][i]-y1_predict[i])
        resid_2.append(data[1][i]-y2_predict[i])
    
    plt.scatter(data[0],resid_1)
    plt.xlabel("Year")
    plt.ylabel("Residual")
    plt.title("Residuals for Linear model")
    plt.savefig("figures/part2_residuals1.pdf", format='pdf')
    plt.show()
    plt.clf()

    plt.scatter(data[0],resid_2)
    plt.xlabel("Year")
    plt.ylabel("Residual")
    plt.title("Residuals for Quadratic model")
    plt.savefig("figures/part2_residuals2.pdf", format='pdf')
    plt.show()
    plt.clf()
    
    #Part 3
    #Using a model for prediction
    new_data = pd.read_csv("data/sea_ice_2013-2020.csv", header=None)
    
    # Scatter plot original data (1979-2012)
    plt.scatter(data[0], data[1], label="Observed (1979-2012)", color='blue')

    # Scatter plot new data (2013-2020)
    plt.scatter(new_data[0], new_data[1], label="Observed (2013-2020)", color='red')

    # Create extended x-values from 1979 to 2020 for predictions
    x_full = np.linspace(1979, 2020, 500)
    
    # Compute model predictions
    y1_full = predict(x_full,deg_1_coef)  # Linear model
    y2_full = predict(x_full,deg_2_coef)# Quadratic model

    # Plot predictions (Linear)
    plt.plot(x_full, y1_full, label="Linear Model", linestyle="--", color='green')
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Sea Ice Extent (Millions of Square Kilometers)")
    plt.title("Sea Ice Extent Prediction (Linear Model)")
    plt.savefig("figures/part3_pred1.pdf", format='pdf')
    plt.show()
    plt.clf()

    # Plot predictions (Quadratic)
    plt.scatter(data[0], data[1], label="Observed (1979-2012)", color='blue')
    plt.scatter(new_data[0], new_data[1], label="Observed (2013-2020)", color='red')
    plt.plot(x_full, y2_full, label="Quadratic Model", linestyle="--", color='purple')
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Sea Ice Extent (Millions of Square Kilometers)")
    plt.title("Sea Ice Extent Prediction (Quadratic Model)")
    plt.savefig("figures/part3_pred2.pdf", format='pdf')
    plt.show()
    plt.clf()


    #Part 4
    #Training Data
    data_4 = pd.read_csv("data/regression_train.csv",header=None)
    #Models
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

    coeffs = [deg_0_coef,deg_1_coef,deg_2_coef,deg_3_coef,deg_4_coef,deg_5_coef,deg_6_coef,deg_7_coef,deg_8_coef,deg_9_coef,deg_10_coef]
    RSS = []
    #plotting each coeff, and also creating RSS values
    x = np.linspace(0,1,100)
    for d,coefficient in enumerate(coeffs):
        predicted_val = predict(x,coefficient)
        plt.scatter(data_4[0],data_4[1])
        plt.xlabel("X values")
        plt.ylabel("Y values")
        plt.title(f"{d} Degrees plot")
        plt.plot(x,predicted_val) # Shows model's predicted curve
        plt.savefig(f"figures/part4_deg{d}.pdf",format = 'pdf')
        plt.clf()
        RSS.append(calc_RSS(data_4[1],predict(data_4[0],coefficient)))

    #Elbow plot
    plt.plot(range(0, len(coeffs)), RSS, marker = 'o', linestyle = '-', color = 'blue')
    plt.xlabel("Polynomial Degree")
    plt.ylabel("Residual Sum of Squares (RSS)")
    plt.title("Elbow Plot of Polynomial Degree vs RSS")
    plt.xticks(range(0, len(coeffs)))
    plt.savefig("figures/part4_elbow.pdf", format = 'pdf')
    plt.show()

################################################################################
# HELPER FUNCTIONS
################################################################################
#helper functions for residual
#predicted y

def predict(x,coeff):
    """
    Calculates the predicted values based on an n-degree model
    takes in x: data values to predict y for
    coeff: coefficients with which to 
    """
    pred = []
    for i in x:
        predicted_value = 0
        for n,c in enumerate(coeff):
            predicted_value+= c*(i**n)
        pred.append(predicted_value)
    return pred


#Calculate RSS
def calc_RSS(x,y):
    """
    Calculates the square of the difference between the actual value and the predicted
    value for each data point.
    takes in x: the true y data values
    y: predicted values from model
    """
    rss = 0
    for i in range(len(x)):
        rss += (x[i]-y[i])**2
    return rss

if __name__ == "__main__":
    main()
