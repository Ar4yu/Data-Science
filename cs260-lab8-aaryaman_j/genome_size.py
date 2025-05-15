"""
Calculates mean difference significance using CLT and permutation testing on genome dataset
Author: Aaryaman Jaising
Date: April 3rd, 2025
"""

import pandas as pd
from scipy.stats import ttest_ind
import random
def read_file(filename):
    df = pd.read_excel(filename,header=0)
    # print(df.shape)
    # print(df["Population"].head())
    # print(df.columns)
    pop1 = df[df["Population"] == 1]["Total Genome Size"]
    pop2 = df[df["Population"] == 2]["Total Genome Size"]
    p1 = pop1.to_list()
    p2 = pop2.to_list()
    return p1,p2
def main():
    p1,p2 = read_file("data/SSuis_Stats.xlsx")
    # print("p1",p1[:3])
    # print("p2",p2[:3])

    result = ttest_ind(p1, p2)
    print(f"CLT p-value: {result[1]:.5f}")

    #permutation testing
    n1 = len(p1)
    p_total = []
    p_total.extend(p1)
    p_total.extend(p2)
    trials = 100000
    diff = abs((sum(p1)/len(p1)) - (sum(p2)/len(p2)))
    extreme_count = 0
    for i in range(trials):
        random.shuffle(p_total)
        p1_tmp = p_total[:n1]
        p2_tmp = p_total[n1:]
        diff_tmp = abs((sum(p1_tmp)/len(p1_tmp)) - (sum(p2_tmp)/len(p2_tmp)))
        if diff_tmp>=diff:
            extreme_count += 1
    p_value = extreme_count/trials
    print(f"Permutation testing p-value: {p_value:.5f}")

    pass

if __name__ == "__main__":
    main()