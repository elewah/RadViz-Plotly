# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:15:37 2020

@author: elewah
"""
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