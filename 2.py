# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 01:30:30 2022

@author: Mohd Ariz Khan
"""
import pandas as pd
df = pd.read_csv("LabTAT.csv")
df
df.head()

# In this case when we have more than two samples we use ANOVA.

df["Laboratory 1"].mean() # select a sample from Laboratory 1
df["Laboratory 2"].mean() # select a sample from Laboratory 2
df["Laboratory 3"].mean() # select a sample from Laboratory 3  
df["Laboratory 4"].mean() # select a sample from Laboratory 4

import scipy.stats as stats
Fcalc, pval = stats.f_oneway(df["Laboratory 1"],df["Laboratory 2"],df["Laboratory 3"],df["Laboratory 4"])
# calculate Fcalculated value and p_value

Fcalc
pval

alpha = 0.05 # 5% significance level

# H0 means there is no difference in average TAT among the different laboratories
# H1 means there is any difference in average TAT among the different laboratories

if p < alpha:
    print("Ho is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")
    
# conclusion: 
# according to Test of Hypothesis, though my sample is not 100% normal.
# H1 is acceptd. so, there is difference in average TAT among the different laboratories.
#========================================================================================