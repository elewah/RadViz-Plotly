# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:10:53 2020

@author: elewah
"""
# =============================================================================
# #Reference used to normilze a column of dataframe 
# #https://stackoverflow.com/questions/53961569/normalize-a-column-of-dataframe-using-min-max-normalization-based-on-groupby-of
# #the normailze function, input X's dataset(attributes matrix), output, norlmized version of the X 
# =============================================================================
def matrixNormlization(X):
    return ((X-X.min())/(X.max()-X.min()))*1