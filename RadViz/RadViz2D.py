# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:40:23 2020

@author: elewah
"""
import pandas as pd
from RadViz._2D_submodules.normalizing import matrixNormlization 
from RadViz._2D_submodules.points_oncircle import get_2Dpoints
from RadViz._2D_submodules.get_anchors_matrix import get_X2Dmatrix
from RadViz._2D_submodules.RadViz_mapping import Radviz2DMapping
from RadViz._2D_submodules.plotly_2Dframe import Dataframe2DPreparation
from RadViz._2D_submodules._2Dscatterplot_plotly import plotRadviz2D

def RadViz2D(y,X,BPs):
    y.rename("index",inplace=True) 
    X=matrixNormlization(X)
    S=X ##change the name to be comptable with the prove (S is the symbol matrix)
    DS_names=S.columns
    X=get_X2Dmatrix(DS_names) # X is DAs matrix
    S_hat=Radviz2DMapping(S,X)
    d=DS_names.size
    df,df_circle =  Dataframe2DPreparation(S_hat,X,d,BPs,y)
    plotRadviz2D(df,df_circle)