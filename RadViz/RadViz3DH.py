# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:40:23 2020

@author: elewah
"""
import pandas as pd
from RadViz._3D_submodules.normalizing import matrixNormlization 
from RadViz._3D_submodules.points_onsphere import get_3Dpoints
from RadViz._3D_submodules.get_anchors_matrix import get_X3Dmatrix
from RadViz._3D_submodules.RadViz_mapping import Radviz3DMapping
from RadViz._3D_submodules._3Dscatterplot_plotly import plotRadviz3D

def RadViz3DH(y,X,BPs):
    y.rename("index",inplace=True) 
    X=matrixNormlization(X)
    S=X ##change the name to be comptable with the prove (S is the symbol matrix)
    DS_names=S.columns
    X=get_X3Dmatrix(DS_names) # X is DAs matrix
    S_hat=Radviz3DMapping(S,X)
    frames = [y,S_hat]
    S_hat = pd.concat(frames,axis=1)
    plotRadviz3D(S_hat)