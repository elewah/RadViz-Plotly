# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:15:37 2020

@author: elewah
"""
# =============================================================================
# #Reference of algorthim that is used distribute the point over sphere 
# #https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere
# #we use The golden spiral method
# #get_3Dpoints function over a sphere,
# #input variable radius of the sphere and number of points, the output is (nX3) cordinates-points matrix in dataframe format
# #where n is number of points and 3 is three columns (x,y,z)  
# =============================================================================

import numpy as np
import pandas as pd
from numpy import pi, cos, sin, arccos, arange

def get_3Dpoints(d):
    indices = arange(0, d, dtype=float) + 0.5
    phi = arccos(1 - 2*indices/d)
    theta = pi * (1 + 5**0.5) * indices
    x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi);
    df = pd.DataFrame({'x': x, 'y': y, 'z': z})
    #print(df)
    return df