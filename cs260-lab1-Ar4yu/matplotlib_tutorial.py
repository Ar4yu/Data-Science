'''
Learn to use matplotlib for plotting, also reading in files
Author: Aaryaman Jaising
Date: January 21, 2025
'''

import matplotlib.pyplot as plt
import numpy as np

################################################################################
# MAIN
################################################################################

def main():
    """
    read in data from the file and create plot accordingly
    Author: Aaryaman Jaising
    Date: 23/01/2025
    """
    user_data = np.loadtxt('data/facebook_users.csv', delimiter=',')
    print(user_data)
    years = user_data[:,0]
    num_users = user_data[:,1]
    plt.scatter(years,num_users,color="black")
    plt.xlabel("Year")
    plt.ylabel("Number of Facebook Users (Millions)")
    plt.title("Annual Facebook Users Statistics")
    y = -432342.27 + 215.39 * years
    plt.plot(years, y, color="blue")
    # plt.savefig("figures/facebook_users.pdf", format='pdf')
    plt.clf()

    quad_coefs = [0, 4, -1]       # y = 4x - x^2
    cubic_coefs = [2, 0, -2, 1]   # y = 2 - 2x^2 + x^3  
    x = np.linspace(0, 5, 100)
    y1 = quad_coefs[0]+quad_coefs[1]*x+quad_coefs[2]*(x**2)
    y2 = cubic_coefs[0] + cubic_coefs[1]*x + cubic_coefs[2]*(x**2) + cubic_coefs[3]*(x**3)
    plt.plot(x, y1, label="Quadratic")
    plt.plot(x, y2, label="Cubic")
    plt.legend()
    plt.title("Quadratic vs Cubic function")
    plt.savefig("figures/quad_cubic.pdf", format='pdf')
    plt.show()
    
if __name__ == "__main__" :
    main()
