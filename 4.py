# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:24:27 2022

@author: Mohd Ariz Khan
"""
import pandas as pd
df = pd.read_csv("Costomer+OrderForm.csv")
df

df.Phillippines.value_counts()
df.Indonesia.value_counts()
df.Malta.value_counts()
df.India.value_counts()

import numpy as np
# Make a contingency table
obs = np.array([[271,267,269,280],[29,33,31,20]])
obs

from scipy.stats import chi2_contingency
# Chi2 contengency independence test
chi2_contingency(obs) # o/p is (Chi2 stats value, p_value, d_o_f, expected obsvations)

# Compare p_value with α = 0.05 because 5% significance level
alpha = 0.05

if 0.27 < alpha:
    print("Ho is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")
    
# conclusion:
# according to Test of Hypothesis,the above data value falls in accepted region.
# so, Ho is accepted means both variables are independent of each others.
#=============================================================================
