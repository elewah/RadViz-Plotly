# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:15:37 2020

@author: elewah
"""
# =============================================================================
# #Reference of algorthim that is used distribute the point over circumferece
# #https://stackoverflow.com/questions/48081690/how-to-find-points-on-a-circumference
# #get_2Dpoints function over a circumference,
# #input variable radius of the circle and number of points, the output is (nX2) cordinates-points matrix in dataframe format 
# #where n is number of points and 2 is two columns (x,y) 
# =============================================================================
import numpy as np
def get_2Dpoints(radius, number_of_points):
    radians_between_each_point = 2*np.pi/number_of_points
    list_of_points = []
    for p in range(0, number_of_points):
        list_of_points.append( (radius*np.cos(p*radians_between_each_point),radius*np.sin(p*radians_between_each_point)) )
    return list_of_points