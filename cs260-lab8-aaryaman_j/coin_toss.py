"""
Coin Toss analysis using central limit theorem and randomized trials
Author: Aaryaman Jaising
Date: April 3rd, 2025
"""
from scipy.integrate import quad
from scipy.stats import norm
import math
import random
import matplotlib.pyplot as plt

def trial(n):
    """
    n is the number of coin flips, returns the sample mean of heads
    """
    heads = 0
    for i in range(n):
        if random.random()>0.5:
            heads+=1
    return heads/n


def main():
    heads = 54
    n = 80
    p_null = 0.5
    pass
    sd = math.sqrt(0.5*(0.25+0.25))
    sample_mean = heads/n

    z_score = (sample_mean - p_null)/math.sqrt((sd**2)/n)
    result, error = quad(norm.pdf,z_score,math.inf)
    p_value = result*2 
    print(f"CLT p-value: {p_value:.5f}")

    #using simulation using random
    n_e = 0
    hist = []
    for i in range(100000):
        #accounting for two tails
        #two sided
        tmp = trial(80)
        hist.append(tmp)
        if tmp >= sample_mean:
            n_e +=1
        elif tmp <= (1-sample_mean):
            n_e += 1
    p_value = n_e/100000
    print(f"Random trials p-value: {p_value:.5f}")

    plt.hist(hist, bins=30, density=True)
    plt.axvline(sample_mean, color='red', linestyle='--', label='Observed Proportion')
    plt.axvline(0.5 - (sample_mean - 0.5), color='red', linestyle='--')
    plt.xlabel('Proportion of Heads')
    plt.ylabel('Density')
    plt.title('Null Distribution of Coin Toss Proportions')
    plt.legend()

    plt.savefig('figures/coin_toss.pdf')
    plt.close()


if __name__ == "__main__":
    main()