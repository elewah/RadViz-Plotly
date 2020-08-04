# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:25:08 2020

@author: elewah
"""

def Radviz3DMapping(S,X):
    S_hat=S.dot(X)  # S.X 
    #print(S_hat)
    S_hat=S_hat.div(S.sum(axis=1), axis=0) # divide by the sum of each row
    return S_hat.fillna(0)