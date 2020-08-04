# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:20:38 2020

@author: elewah
"""
# =============================================================================
# #get_Xmayrix function is designed to return X matrix "Dimension anchors matrix"
# #input is the number of atterbutes, output is X matrix (Dimension anchors matrix)
# =============================================================================

import pandas as pd
from RadViz._2D_submodules.points_oncircle import get_2Dpoints

def get_X2Dmatrix(DS_names):
    DS_names=pd.DataFrame(DS_names)
    DS_names = DS_names.rename(columns={0: 'DS_names'})
    d=DS_names.size
    DS=get_2Dpoints(1, d)
    DS= pd.DataFrame(DS).round(6)
    frames=frames = [DS_names,DS]
    X = pd.concat(frames,axis=1)
    X= X.set_index('DS_names')
    X.index.name = None
    return X