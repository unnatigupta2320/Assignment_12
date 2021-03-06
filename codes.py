import numpy as np
import matplotlib.pyplot as plt

def bayes_theorem(p_e1,p_e2,p_xgiven_e1,p_xgiven_e2):
	p_x= p_e1*p_xgiven_e1 + p_e2*p_xgiven_e2
	numerator1 = p_e1*p_xgiven_e1
	p_e1given_x=numerator1/p_x
	return p_e1given_x

#Probability that second group wins
p_1= 0.4
#Probability that the first group wins
p_2= 0.6
#Probability that new product is introduced if second group wins
pnew_1=0.3
#Probability that new product is introduced if first  group wins
pnew_2= 0.7

#Probability that new product is introduced by second group 
prob= bayes_theorem(p_1,p_2,pnew_1,pnew_2)

print(prob)
