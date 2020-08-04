# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:40:23 2020

@author: elewah
"""
import numpy as np
import pandas as pd
import plotly.express as px
from numpy import pi, cos, sin, arccos, arange
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
# =============================================================================
# 
# =============================================================================
from RadViz._2D_submodules.normalizing import matrixNormlization 
from RadViz._2D_submodules.points_oncircle import get_2Dpoints
from RadViz._2D_submodules.get_anchors_matrix import get_X2Dmatrix
from RadViz._2D_submodules.RadViz_mapping import Radviz2DMapping
from RadViz._2D_submodules.plotly_2Dframe import Dataframe2DPreparation
from RadViz._2D_submodules._2Dscatterplot_plotly import plotRadviz2D
# =============================================================================
# 
# =============================================================================
from RadViz._3D_submodules.normalizing import matrixNormlization 
from RadViz._3D_submodules.points_onsphere import get_3Dpoints
from RadViz._3D_submodules.get_anchors_matrix import get_X3Dmatrix
from RadViz._3D_submodules.RadViz_mapping import Radviz3DMapping
from RadViz._3D_submodules.plotly_3Dframe import Dataframe3DPreparation
from RadViz._3D_submodules._3Dscatterplot_plotly import plotRadviz3D
# =============================================================================
#RadViz2D  is designed to be the main 2D Radviz function
#It has three input y(labels column), X(features dataframe) and BPs (number of Boundaries' points)
#the output of this function is 2D RadViz plot
#mainly this function handles the whole process of Data visualization using the introduced RadViz algorithm(2D version
# =============================================================================


def RadViz2D(y,X,BPs):
    y.rename("index",inplace=True) 
    #print(X)
    #print(100*'*')
    X=matrixNormlization(X)
    #print(X)
    S=X ##change the name to be comptable with the prove (S is the symbol matrix)
    #print("S matrix")
    #print(S)
    #print("*"*100)
    DS_names=S.columns
    X=get_X2Dmatrix(DS_names) # X is DAs matrix
    #print("*"*100)
    #print("X matrix")
    #print(X)
    #print("*"*100)
    S_hat=Radviz2DMapping(S,X)
    #print("*"*100)
    #print("S_hat matrix")
    #print(S_hat)
    d=DS_names.size
    df = Dataframe2DPreparation(S_hat,X,d,BPs,y)
    plotRadviz2D(df)
    
# =============================================================================
#RadViz3D  is designed to be the main 3D Radviz function
#It has three input y(labels column), X(features dataframe) and BPs (number of Boundaries' points)
#the output of this function is 3D RadViz  plot
#mainly this function handles the whole process of Data visualization using the introduced RadViz algorithm(3D version)
# =============================================================================
 
def RadViz3D(y,X,BPs):
    #print(X)
    #print(100*'*')
    y.rename("index",inplace=True) 
    X=matrixNormlization(X)
    #print(X)
    S=X ##change the name to be comptable with the prove (S is the symbol matrix)
    #print("S matrix")
    #print(S)
    #print("*"*100)
    DS_names=S.columns
    X=get_X3Dmatrix(DS_names) # X is DAs matrix
    #print("*"*100)
    #print("X matrix")
    #print(X)
    #print("*"*100)
    S_hat=Radviz3DMapping(S,X)
    #print("*"*100)
    #print("S_hat matrix")
    #print(S_hat)
    d=DS_names.size
    df = Dataframe3DPreparation(S_hat,X,d,BPs,y)
    plotRadviz3D(df)
   
# =============================================================================
#RadViz3D  is designed to be the main 3D Radviz function (Bar color) used when y are numerical values and not catgories
#It has three input y(labels column), X(features dataframe) and BPs (number of Boundaries' points)
#the output of this function is 3D RadViz  plot
#mainly this function handles the whole process of Data visualization using the introduced RadViz algorithm(3D version)
# =============================================================================

def RadViz3DH(y,X,BPs):
    #print(X)
    #print(100*'*')
    y.rename("index",inplace=True) 
    X=matrixNormlization(X)
    #print(X)
    S=X ##change the name to be comptable with the prove (S is the symbol matrix)
    #print("S matrix")
    #print(S)
    #print("*"*100)
    DS_names=S.columns
    X=get_X3Dmatrix(DS_names) # X is DAs matrix
    #print("*"*100)
    #print("X matrix")
    #print(X)
    #print("*"*100)
    S_hat=Radviz2DMapping(S,X)
    #print("*"*100)
    #print("S_hat matrix")
    #print(S_hat)
    frames = [y,S_hat]
    S_hat = pd.concat(frames,axis=1)
    plotRadviz3D(S_hat)
  
# =============================================================================
# for testing purpose     
# =============================================================================

#BreastCancer
# =============================================================================
# import plotly.io as pio
# pio.renderers.default = "browser"   
# data= pd.read_csv('DataFolder/BreastCancer.csv')
# y=data['index']
# X=data.drop(['index'], axis=1)
# BPs=10000
# RadViz3D(y,X,BPs)
# RadViz2D(y,X,BPs)  
# =============================================================================

