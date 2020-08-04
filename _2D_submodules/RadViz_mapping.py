# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:25:08 2020

@author: elewah
"""
# =============================================================================
# # this 2D Radviz function is created to get the S_hat matrix (2D-RadViz mapped versions of samples)
# #inputs are S matrix(samples or Records matrix) and X matrix (dimensions' anchors matrix) 
# =============================================================================
def Radviz2DMapping(S,X):
    S_hat=S.dot(X)  # applying matrix multiplication S.X where 
    #print(S_hat)
    S_hat=S_hat.div(S.sum(axis=1), axis=0) # divide by SUMX (the sum of each row vector) S_hat=S.X/SUMX
    return S_hat.fillna(0) #to solve divided by 0 problem (sumation problem incase all attributes value equal to 0) 