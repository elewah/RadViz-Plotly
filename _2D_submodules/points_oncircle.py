# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:15:37 2020

@author: elewah
"""
import numpy as np
def get_2Dpoints(radius, number_of_points):
    radians_between_each_point = 2*np.pi/number_of_points
    list_of_points = []
    for p in range(0, number_of_points):
        list_of_points.append( (radius*np.cos(p*radians_between_each_point),radius*np.sin(p*radians_between_each_point)) )
    return list_of_points