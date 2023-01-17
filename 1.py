# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 01:04:45 2022

@author: Mohd Ariz Khan
"""
import pandas as pd
df = pd.read_csv("Cutlets.csv")
df
df.head()

df["Unit A"].mean() # select a sample from unit A 
df["Unit B"].mean() # select a sample from unit B


from scipy import stats as twosample
zcalc ,pval = twosample.ttest_ind( df["Unit A"] , df["Unit B"] ) # calculate zcalculated value and p_value

print("zcalculated value: ",zcalc)
print("p-value: ",pval)

alpha = 0.05 # 5% significance level

# H0 means the diameter of both the cutlets is same.
# H1 means the diameter of both the cutlets is not same.

if pval<alpha:
    print("Ho is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")
    
# conclusion: 
# according to Test of Hypothesis, though my sample is 100% normal.
# so, we can claim that the above data is really following normal.#
# H0 is acceptd. so, the diameter of both the cutlets is same.
#===================================================================