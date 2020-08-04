# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:10:53 2020

@author: elewah
"""

def matrixNormlization(X):
    return ((X-X.min())/(X.max()-X.min()))*1